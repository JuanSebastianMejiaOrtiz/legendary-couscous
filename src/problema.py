import numpy as np
import funciones as fn
import matplotlib.pyplot as plt


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


t1, y1 = fn.forwardEuler(f1, [theta0, 0], 0, 5)
t2, y2 = fn.forwardEuler(f2, [theta0, 0], 0, 5)

plt.plot(t1, y1[:, 0], label=r"$\theta$ sin resistencia")
plt.plot(t2, y2[:, 0], label=r"$\theta$ con resistencia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Ángulo (rad)")
plt.legend()
plt.grid()
plt.show()
