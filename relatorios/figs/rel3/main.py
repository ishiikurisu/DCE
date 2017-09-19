import scipy
import scipy.signal
import matplotlib.pyplot
import numpy

def apply(t, f):
    return t, list(f(t))

def plot(t, f, lx, ly, w):
    matplotlib.pyplot.plot(t, f)
    matplotlib.pyplot.ylabel(ly)
    matplotlib.pyplot.xlabel(lx)
    matplotlib.pyplot.savefig(w)
    matplotlib.pyplot.clf()

def ex1():
    return apply(numpy.linspace(0, 10, 100),
                 lambda t: map(lambda y: y if y > 0 else 0, numpy.sin(t)))

def ex2():
    return apply(numpy.linspace(-5, 5, 100),
                 lambda t: map(lambda y: y if y > 0 else 0, t))

def ex5():
    return apply(numpy.linspace(-5, 5, 100),
                 lambda t: map(lambda y: y -1.1 if y > 1.1 else 0, t))

def ex6():
    def f(t):
        vf = 1.1
        if t > vf:
            return vf
        elif t < -vf:
            return -vf
        else:
            return 0
    return apply(numpy.linspace(-5, 5, 100),
                 lambda t: map(lambda y: f(y), t))

if __name__ == '__main__':
    t, v_o = ex1()
    plot(t, v_o, 'Tempo', 'Tensão', 'ex1.png')
    v_i, v_o = ex2()
    plot(v_i, v_o, 'Vi', 'Vo', 'ex2.png')
    v, v_s = ex5()
    plot(v, v_s, 'V', 'Vs', 'ex5.png')
    v, v_s = ex6()
    plot(v, v_s, 'V', 'Vs', 'ex6.png')
