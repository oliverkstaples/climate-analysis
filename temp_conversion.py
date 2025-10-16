# Todo: Code is a bit unclear

def F_to_C(x):
    Y = (x - 32) * (5 / 9)
    return Y

def FK(x):
    y = F_to_C(x)
    z = y + 273.15
    return z
