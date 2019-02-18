from math import exp as e

def largrandian_interpolation(points, x='x'):
    """
    :param points: a list of points ex: ((0,1),(1,2))
    :param x: a given x value to get y value of
    :return: y value of x given
    """
    if not (type(x) is str):
        x = float(x)
    print("P{0}({1}) = ".format(len(points) - 1, x), end="")
    def L(i):
        ret = 1
        xi = points[i][0]
        for j in range(len(points)):
            if i != j:
                if type(x) is float:
                    ret *= (x - points[j][0])
                print("({0} - {1})".format(x, points[j][0]), end="")
        print("/", end="")
        for j in range(len(points)):
            if i != j:
                if type(x) is float:
                    ret /= (xi - points[j][0])
                print("({0} - {1})".format(xi, points[j][0]), end="")
        return ret
    ret = 0
    for i in range(len(points)):
        print("{0}*".format(points[i][1]), end="")
        ret += points[i][1] * L(i)
        if i + 1 < len(points):
            print(" + ", end="")
    if type(x) == float:
        print(" = {0}".format(ret))
        return ret
    return ""


print(largrandian_interpolation(((1.2,1.5095),(1.3,1.6984),(1.4,1.9043),(1.5,2.1293),(1.6,2.3756)),1.1))
x=1.1
print((e(x) - e(-x))/2)
print()
print(largrandian_interpolation(((1.2,1.5095),(1.3,1.6984),(1.4,1.9043),(1.5,2.1293),(1.6,2.3756)),1.3))
x=1.3
print((e(x) - e(-x))/2)
print()
print(largrandian_interpolation(((1.2,1.5095),(1.3,1.6984),(1.4,1.9043),(1.5,2.1293),(1.6,2.3756)),1.6))
x=1.6
print((e(x) - e(-x))/2)