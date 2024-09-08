import matplotlib.pyplot as plt
import time, math

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
        else: return self.s_rand(tm)

cs = 70
x = [int(Randomise(cs + i).result) for i in range(60)]
y = [int(i) for  i in range(60)]

plt.plot(x, y, 'bo-', label='Line Plot')
plt.title('Randomise Numbers With Current Second')
plt.xlabel('Generated Number')
plt.ylabel('Time (sec)')
plt.legend()
plt.show()
