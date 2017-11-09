import numpy as np
import matplotlib.pyplot as plt

def load(where):
    first_line = True
    data = { }
    fields = [ ]

    with open(where, 'r') as fp:
        for line in fp:
            if first_line:
                fields = list(map(lambda s: s.strip(), line.split('\t')))
                for field in fields:
                    data[field] = []
                first_line = False
            else:
                rows = list(map(float, map(lambda s: s.replace(',', '.'), line.split('\t'))))
                for i, field in enumerate(fields):
                    data[field].append(rows[i])

    return data

def draw(data, what):
    lines = []
    all_v_cc = data['v_cc']
    all_what = data[what]
    i_c = data['i_c']
    all_v = {}
    all_i = {}
    lines = []

    for i, v_cc in enumerate(all_v_cc):
        if str(v_cc) not in all_v:
            all_v[str(v_cc)] = []
            all_i[str(v_cc)] = []
        all_v[str(v_cc)].append(all_what[i])
        all_i[str(v_cc)].append(i_c[i])

    for v_cc in all_v:
        i = all_i[str(v_cc)]
        v = all_v[str(v_cc)]
        curve_label = 'v_cc = %.4f' % (float(v_cc))
        line, = plt.plot(i, v, label=curve_label)
        lines.append(line)

    plt.legend(handles=lines)
    plt.xlabel('i_c (mA)')
    plt.ylabel('{0} (V)'.format(what))
    plt.savefig('{0}.png'.format(what))
    plt.clf()

if __name__ == '__main__':
    data = load('figs/rel5/dados.csv')
    draw(data, 'v_be')
    draw(data, 'v_ce')
