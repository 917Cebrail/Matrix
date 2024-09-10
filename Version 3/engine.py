import math, struct

pi = 3.14

class Randomise:
    def s_rand(self, nxt):
        nxt = nxt * 1103515245 + 12345
        return int(((nxt / 65536) % 32768))

    def square_root(self, x):
        if x == 0: return 1 / math.sqrt(x + 1)
        else: return 1 / math.sqrt(x)

    def s_f(self, x):
        if x == 0: return math.acos(1 / (x + 1))
        else: return math.acos(1 / x)

    def __init__(self, tm, sel):
        self.result = self.compute(tm, sel)

    def compute(self, tm, sel):
        if sel != 1:
            if tm % 3 == 0: return self.s_rand(self.s_f(tm))
            elif tm % 2 == 0: return self.s_rand(self.square_root(tm))
            else: return self.s_rand(tm)
        else:
            if tm % 2 == 0:
                return int(self.s_rand(self.square_root(tm)))
            elif tm % 2 != 0 and tm % 3 == 0:
                return int(self.s_rand(tm))
            elif [tm % 2 != 0 , tm % 3 != 0] and tm % 4 == 0:
                return int(self.square_root(self.s_rand(tm)))
            elif [tm % 2 != 0 , tm % 3 != 0 , tm % 4 != 0] and tm % 5 == 0:
                return int(self.s_rand(q_rsqrt(tm)))
            else:
                return int(self.s_rand(tm))

def s_digit(x):
    return [int(digit) for digit in str(x)]

def square_root(x):
    if x == 0: return 1 / math.sqrt(x+1)
    else : return 1 / math.sqrt(x)

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

def s_dec_digit(nxt):
    print("%.2f" % nxt)

#Ending Randomise class era

def s_light(I, x0, y0, x1, y1):
    dx = abs(x1+2 - x0)
    dy = abs(y1+2 - y0)
    hyp = math.sqrt(dx**2 + dy**2)
    if hyp == 0:
        angle = 0
    else:
        angle = math.atan2(dy, dx)

    e = (I / dx + 1) * math.sin((angle + 1))

    #print("E : %.1f" % e)
    #print("\\-> [I] I:", I, ", dx:", dx, " dz:", dy, " hyp:", hyp, " ANGLE:", math.degrees(angle))
    return e

def s_lum(I): return 4 * pi * I
