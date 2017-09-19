import scipy
import scipy.signal
import matplotlib.pyplot
import numpy

def apply(t, f):
    return t, list(f(t))

def ex1():
    return apply(numpy.linspace(0, 10, 100),
                 lambda t: map(lambda y: y if y > 0 else 0, numpy.sin(t)))

def ex2():
    return apply(numpy.linspace(-5, 5, 100),
                 lambda t: map(lambda y: y if y > 0 else 0, t))

if __name__ == '__main__':
    t, v_o = ex1()
    matplotlib.pyplot.plot(t, v_o)
    matplotlib.pyplot.ylabel('Tensão')
    matplotlib.pyplot.xlabel('Tempo')
    matplotlib.pyplot.savefig('ex1.png')
    matplotlib.pyplot.clf()

    t, v_o = ex2()
    matplotlib.pyplot.plot(t, v_o)
    matplotlib.pyplot.ylabel('Vo')
    matplotlib.pyplot.xlabel('Vi')
    matplotlib.pyplot.savefig('ex2.png')
    matplotlib.pyplot.clf()
