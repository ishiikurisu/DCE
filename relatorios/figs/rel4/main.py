def ex4():
    v = 10
    r = 500
    v_z = 9.1
    i_z = 28E-3
    z_z = 5
    v_zo = v_z - i_z*z_z
    i_z = (v-v_zo)/(r+z_z)
    e_0 = v - i_z*r
    r_l = (e_0*r)/(v-e_0)
    print("R_L = %.3f" % (r_l))

def ex9():
    f = 60
    c = 220E-6
    I = 1
    v = I/2/f/c
    print("v_pp = %3.f" % (v))

if __name__ == '__main__':
    print("--- # Exercício 4")
    ex4()
    print("--- # Exercício 9")
    ex9()
    print("...")
