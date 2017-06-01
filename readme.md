# PyTimer
## How to Install

Directly install:

    pip install git+https://github.com/RalphMao/PyTimer.git

Or clone and install:

    git clone https://github.com/RalphMao/PyTimer.git
    cd PyTimer
    pip install -r requirements.txt
    python setup.py install --user --record files.txt


## Basic Usage

***Timer*** Create a timer instance which can either work as a decorator or a normal object. One can choose to report average or the last timing results by setting the initialization args. Available arguments:
**average** enables you to average the timing results of all epochs.
**logger** enables you to direct the output to other locations or in other format.
**namespace** helps when you have multiple timers work together.

**Timer.restart**  Start a new timing epoch. Clear all temporary states and add the epoch counter.

**Timer.reset** Set the start as the current time.

**Timer.checkpoint** Measure and (optionally)cumulate the timing.

**Timer.summary** will report the lengths of every interval (of the current epoch or the average of all epochs). By setting argument
**name** you can choose to report only one interval

### How it works
![](https://raw.githubusercontent.com/RalphMao/PyTimer/master/pytimer.png)

## Basic Usage

### Embed into codes

    from pytimer import Timer
    timer = Timer()                                           
    def any_function():                                       
        timer.start()                                         

        for i in range(10):                                   

            timer.reset()                                     
            np.dot(np.ones((100,1000)), np.zeros((1000,500)))
            timer.checkpoint('block1')                        

            np.dot(np.ones((100,1000)), np.zeros((1000,500)))
            np.dot(np.ones((100,1000)), np.zeros((1000,500)))
            timer.checkpoint('block2')                        
            np.dot(np.ones((100,1000)), np.zeros((1000,1000)))

        for j in range(20):                                   
            np.dot(np.ones((100,1000)), np.zeros((1000,500)))
        timer.summary()                                       

    any_function()                                            
    for i in range(5):                                        
        any_function()                                        

### Decorator

    from pytimer import Timer
    @Timer(average=False, namespace='Function A')      
    def matmul(a,b, times=100):
        for i in range(times):
            np.dot(a,b)        

    matmul(np.ones((100,1000)), np.zeros((1000,500)))            
    matmul(np.ones((100,1000)), np.zeros((1000,500)), times=1000)


## Advanced Usage

During Timer initialization:

