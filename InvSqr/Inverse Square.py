import struct, math
import matplotlib.pyplot as plt
import numpy as np

class Randomise:
    def __init__(self, tm):
        self.result = self.compute(tm)

    def s_rand(self, nxt):
        return int(((nxt * 1103515245 + 12345) / 65536) % 32768)

    def square_root(self, x):
        return 1 / math.sqrt(x) if x != 0 else 1
    
    def compute(self, tm):
        if tm % 2 == 0: return self.s_rand(self.square_root(tm))
        elif tm % 2 != 0 and tm % 3 == 0 : return self.s_rand(tm)
        elif [tm % 2 != 0 , tm % 3 != 0] and tm % 4 == 0 : self.square_root(self.s_rand(tm))
        elif [tm % 2 != 0 , tm % 3 != 0 , tm % 4 != 0] and tm % 5 == 0 : self.s_rand(q_rsqrt(tm))
        else: return self.s_rand(tm)

def q_rsqrt(number):
    if number <= 0:
        return 0
    x2 = number * 0.5
    y = number
    i = struct.unpack('l', struct.pack('f', y))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('f', struct.pack('l', i))[0]
    y = y * (1.5 - (x2 * y * y))
    return y

cs = 65
x = [(Randomise(cs + i).result) for i in range(60)]
y = [int(i) for  i in range(60)]

plt.plot(x, y, 'bo-', label='Inverse Square Root Plot')
plt.title('Inverse Square Root Approximation')
plt.xlabel('Approximation of 1/sqrt(x)')
plt.ylabel('Index')
plt.legend()
plt.grid(True)
plt.show()
