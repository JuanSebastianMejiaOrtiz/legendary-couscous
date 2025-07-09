import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def plot(f, y0, a, b, n=100, method='forwardEuler'):
    t_eval = np.linspace(a, b, n)
    solutions = []
    for func in f:
        if method == 'forwardEuler':
            t, y = forwardEuler(func, y0, a, b, n)
        else:  # Métodos de solve_ivp
            sol = solve_ivp(func, [a, b], y0, method=method, t_eval=t_eval)
            t, y = sol.t, sol.y.T
        solutions.append((t, y))

    # Configurar gráficos
    plt.plot(solutions[0][0], solutions[0][1][:, 0],
             label=r"$\theta$ sin resistencia")
    plt.plot(solutions[1][0], solutions[1][1][:, 0],
             label=r"$\theta$ con resistencia")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Ángulo (rad)")
    plt.legend()
    plt.grid()
    plt.title(f"Método: {method}")


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
