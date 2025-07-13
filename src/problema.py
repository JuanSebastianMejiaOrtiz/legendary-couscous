import numpy as np
import matplotlib.pyplot as plt
import testing as test
import os

g = 9.81  # Aceleración de la gravedad
L = 1  # Longitud. Cambiar cuando sea debido
# Cuando resistencia del aire se considera
m = 1  # Masa. Cambiar cuando sea debido
c = 1  # Coeficiente de fricción. Cambiar cuando sea debido

objeto = ['anillo1', 'anillo2', 'cosoMetal1', 'cosoMetal2']

print("Theoretical analysis")
base_dir = "build/figs/theoretical"
for obj in objeto:
    os.makedirs(os.path.join(base_dir, obj), exist_ok=True)


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
a, b = 0, 10
n = 200
methods = ['forwardEuler', 'RK45', 'BDF', 'LSODA']

# Anillo 1
theta0 = np.radians(45)
m = test.gramsTokilograms(0.5)

c = 6e-8

y0 = [theta0, 0]
for method in methods:
    plt.figure()
    test.plot(f, y0, a, b, n, method, objeto[0])
    plt.savefig(
        f"{base_dir}/{objeto[0]}/{objeto[0]}_{method}_with_n_{n}.png")
print(f"Done with {objeto[0]}")

# Anillo 2
L = 0.45
for method in methods:
    plt.figure()
    test.plot(f, y0, a, b, n, method, objeto[1])
    plt.savefig(
        f"{base_dir}/{objeto[1]}/{objeto[1]}_{method}_with_n_{n}.png")
print(f"Done with {objeto[1]}")


# Coso de metal 1
theta0 = np.radians(60)
m = test.gramsTokilograms(86)
L = 0.5

c = 4e-4
# c = 0.00211

y0 = [theta0, 0]
for method in methods:
    plt.figure()
    test.plot(f, y0, a, b, n, method, objeto[2])
    plt.savefig(
        f"{base_dir}/{objeto[2]}/{objeto[2]}_{method}_with_n_{n}.png")
print(f"Done with {objeto[2]}")

# Coso de metal 2
theta0 = np.radians(50)
y0 = [theta0, 0]
L = 0.3
for method in methods:
    plt.figure()
    test.plot(f, y0, a, b, n, method, objeto[3])
    plt.savefig(
        f"{base_dir}/{objeto[3]}/{objeto[3]}_{method}_with_n_{n}.png")
print(f"Done with {objeto[3]}")

# plt.show()
print("All done")
