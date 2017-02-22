
from pytimer import Timer
import numpy as np

@Timer(average=False)
def matmul(a,b, times=100):
    for i in range(times):
        np.dot(a,b)

matmul(np.ones((100,1000)), np.zeros((1000,500)))
matmul(np.ones((100,1000)), np.zeros((1000,500)), times=1000)

timer = Timer()
for i in range(20):
    timer.start()
    np.dot(np.ones((100,1000)), np.zeros((1000,500)))
    timer.checkpoint(name='block1')

    np.dot(np.ones((100,1000)), np.zeros((1000,500)))
    np.dot(np.ones((100,1000)), np.zeros((1000,500)))
    timer.checkpoint(reset_time=False)

    np.dot(np.ones((100,1000)), np.zeros((1000,500)))

    timer.reset()
    np.dot(np.ones((100,1000)), np.zeros((1000,500)))
    timer.checkpoint(summary=True)

timer.summary()

timer = Timer(average=False)
def a_function():
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

a_function()
for i in range(5):
    a_function()
