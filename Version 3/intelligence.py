import math, engine

function = lambda n,atm,i: 1 / (1 + math.exp(-((n * atm) + engine.square_root(i))))

def expample():
    for i in range(10):
        print("N: " , i , " I: " , i + (i * 0.2) , " atm: " , i*0.5)
        print("\\-> %.2f" % function(i, (i+(i * 0.2)), (i*0.5)))
        print("")
    print("======================")
    """
    for j in range(5):
        code = ["FATGC", "FATTA", "FTACG", "FCGGC", "FTAAT"]
        print(Logic(DNA(code[j])))
    """

# ==================================================================================
# O R G A N I S M
"""
def Strings(c, h, n, o, p):
    if(c == 5 and h == 5 and n == 5 and o == 0 and p == 0): return 'A'
    elif(c == 5 and h == 6 and n == 2 and o == 2 and p == 0): return 'T'
    elif(c == 5 and h == 5 and n == 5 and o == 1 and p == 0): return 'G'
    elif(c == 4 and h == 5 and n == 3 and o == 1 and p == 0): return 'S'
    elif(p == 1 and o == 5) : return 'F'
    else: return 'N'

def String(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4

def DNA(line):
    print("Code : " , line)
    if line == "FATGC":
        return "Starting"
    elif line == "FTAAT":
        return "Ending"
    elif line == "FATTA":
        return "Function1"
    elif line == "FTACG":
        return "Function2"
    elif line == "FCGGC":
        return "Sensors"
    else:
        return "Error : Nucleodide or Phosphate , missing or uncalled"

def Sensors(w, i, b, t):
    return ((w * i + b) / t)

def F1(w, i, b):
    return (((w * i + b) / (w + i + b)) - 1)

def F2(w, i, b):
    return (((w * i - b) * (w - i - b)) / 42)

def Logic(line):
    if line == "Function1": return abs(F1(10, 1, 5))
    elif line == "Function2": return abs(F2(10, 1, 5))
    elif line == "Sensors": return abs(Sensors(10, 1, 1, 32))
    else: return print("Error : Undefined Logic Code")
"""
#Neural Network
