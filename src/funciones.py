import numpy as np


def forwardEuler(f, y0, a, b, n=100):
    if a > b:
        raise ValueError("Starting point can't be greater than final point")

    h = (b - a) / n
    t = np.linspace(a, b, n + 1)
    y = np.empty((len(t), len(y0)))
    y[0] = y0

    for i in range(n):
        y[i + 1] = y[i] + h * np.array(f(t[i], y[i]))

    return t, y
