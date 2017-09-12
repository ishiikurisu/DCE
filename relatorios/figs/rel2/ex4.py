import scipy
import scipy.signal
import matplotlib.pyplot

if __name__ == '__main__':
    A_0 = 1000000
    R_1 = 1000
    R_2 = 10000
    w_b = 3E9 * 2 * scipy.pi

    num = [A_0 * (R_1 + R_2)]
    den = [w_b*(R_1+R_2), R_1+R_2+A_0*R_1]
    sys = scipy.signal.TransferFunction(num, den)
    w, mag, phase = scipy.signal.bode(sys)
    matplotlib.pyplot.figure()
    matplotlib.pyplot.semilogx(w, mag)    # Bode magnitude plot
    matplotlib.pyplot.figure()
    matplotlib.pyplot.semilogx(w, phase)  # Bode phase plot
    matplotlib.pyplot.show()
