'''
Author: Huizi Mao
Email: ralphmao95 at gmail.com
Date: Wed Feb 22 15:26:39 2017
'''
import colorlog
import time
from collections import defaultdict

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(message)s'))
logger = colorlog.getLogger('[%s]'%__file__)
logger.addHandler(handler)
logger.setLevel(15)
default_logger = logger

class Timer(object):
    '''
    Create a timer instance which can either work as a decorator or a normal object
    Args:
    average: Set it to True to average the timing results of all epochs
    logger: The default logger to use. Set it to None to disable printing results
    namespace: Name of the timer
    '''
    def __init__(self, average=True, logger=default_logger, namespace="Default Timer"):
        self.start_time = time.time()
        self.n = 0
        self.cum_time = defaultdict(float)
        self.cur_time = defaultdict(float)
        self.checkpoint_id = 0
        self.average = average
        self.namespace = namespace
        self.logger = logger

    def __call__(self, func):
        def func_wrapper(*args, **kwargs):
            self.start()
            func(*args, **kwargs)
            self.checkpoint(name=func.func_name)
            self.summary()
        return func_wrapper

    def start(self):
        '''
        Start a new timing epoch. Clear all temporary states and add the epoch counter.
        args: None
        '''
        self.start_time = time.time()
        self.n += 1
        self.checkpoint_id = 0
        self.cur_time = defaultdict(float)

    def checkpoint(self, name=None, reset_time=True, summary=False):
        '''
        Measure and (optionally) cumulate and report the timing.
        Args: 
        name: checkpoints with the same name will be cumulated
        reset_time: call reset() after checkpoint
        summary: call summary(name=name) after checkpoint
        '''
        cname = str(self.checkpoint_id) if name is None else name
        interval = time.time() - self.start_time
        self.cur_time[cname] += interval
        self.cum_time[cname] += interval
        if reset_time:
            self.start_time = time.time()
        if name is None:
            self.checkpoint_id += 1
        if summary:
            self.summary(cname)

    def reset(self):
        '''
        Set self.start_time to the current time.
        '''
        self.start_time = time.time()

    def summary(self, name=None):
        '''
        Report the (average or last) timing results, which depends on the setting
        '''
        if self.logger is None:
            return 
        if name is None:
            logger.info("========Summary of %s========"%self.namespace)
            for key in self.cum_time:
                self.summary(name=key)
            logger.info("===================%s========"%("=" * len(self.namespace)))
        else:
            if self.average:
                time = self.cum_time[name] / self.n
            else:
                time = self.cur_time[name]
            logger.info("%10s:%.6f"%(name, time))

