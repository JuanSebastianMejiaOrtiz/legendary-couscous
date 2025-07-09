import numpy as np
import matplotlib.pyplot as plt
import testing as test

theta0 = np.radians(35)
g = 9.81
L = 1
# Cuando resistencia del aire se considera
m = 0.2
c = 0.1


def f1(t, y):
    return [
        y[1],
        -g/L * np.sin(y[0])
    ]


def f2(t, y):
    return [
        y[1],
        -g/L * np.sin(y[0]) - c/(L*m*m) * y[1]
    ]


f = [f1, f2]
y0 = [theta0, 0]
a, b = 0, 10
n = 200
methods = ['forwardEuler', 'RK45', 'BDF', 'LSODA']

for method in methods:
    plt.figure()
    test.plot(f, y0, a, b, n, method)
    plt.savefig(f"build/figs/{method}_with_n_{n}_c_{c}.png")

plt.show()
