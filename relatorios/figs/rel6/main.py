import sympy
import sympy.solvers
from sympy.abc import *

def test():
    solution = sympy.solvers.solve([x+y+1,2*x-y+2], x, y)
    print(solution)

def actual_problem():
    eq1 = x*(1/c+1/o) - y/o + i*beta - 1
    eq2 = x*(1/o) - y*(1/o+1/pi) - z/pi + i*beta
    eq3 = y/pi - z*(1/pi+1/b)
    eq4 = -y/pi + z/pi - i
    solution = sympy.solvers.solve([eq1, eq2, eq3, eq4], x, y, z, i)
    print(solution[x])

if __name__ == '__main__':
    actual_problem()
