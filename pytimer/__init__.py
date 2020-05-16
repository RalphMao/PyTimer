
from pytimer.timer import Timer

_timer_pool = {}

def get_timer(name, **kwargs):
    if name not in _timer_pool:
        _timer_pool[name] = Timer(namespace=name, **kwargs)
    return _timer_pool[name]
