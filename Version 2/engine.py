import math

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

    def __init__(self, tm):
        self.result = self.compute(tm)

    def compute(self, tm):
        if tm % 3 == 0: return self.s_rand(self.s_f(tm))
        elif tm % 2 == 0: return self.s_rand(self.square_root(tm))
        else: return self.s_rand(tm)

def s_digit(x):
    return [int(digit) for digit in str(x)]

# cs = Randomise(time.localtime().tm_sec)  # Getting time
# print(cs.result)                         # Showing result
# print(s_digit(cs.result))                # Showing digits of result
# for digit in s_digit(cs.result):
#    print(digit)                          # Showing and using all digits

def square_root(x):
    if x == 0: return 1 / math.sqrt(x+1)
    else : return 1 / math.sqrt(x)

def s_dec_digit(nxt):
    print("%.2f" % nxt)

def s_light(I, x0, y0, x1, y1):
    dx = abs(x1+2 - x0)
    dy = abs(y1+2 - y0)
    hyp = math.sqrt(dx**2 + dy**2)
    if hyp == 0:
        angle = 0
    else:
        angle = math.atan2(dy, dx)

    e = (I / dx) * math.sin(angle)

    print("E : %.1f" % e)
    print("\\-> [I] I:", I, ", dx:", dx, " dz:", dy, " hyp:", hyp, " ANGLE:", math.degrees(angle))
    return e

def s_lum(I): return 4 * pi * I
