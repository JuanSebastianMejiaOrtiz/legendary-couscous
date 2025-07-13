import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cubicSplines import cubicSplinesInterpolation
import os


def getDataFromCSV(path):
    data = pd.read_csv(path)

    time = data["time"].values
    angleDeg = data["angleDegrees"].values
    return time, np.radians(angleDeg)


def plotData(x, f, label, title, n=200):
    x_eval = np.linspace(min(x), max(x), n)
    plt.plot(x_eval, f(x_eval), label=label)
    plt.xlabel(r'Tiempo ($s$)')
    plt.ylabel(r'Angulo ($rad$)')
    plt.title(title)
    plt.legend()
    plt.grid(True)


def pendulumAnalysis(name):
    file_path = f"./public/experimentalData/{name}.csv"
    time, angle = getDataFromCSV(file_path)
    f = cubicSplinesInterpolation(time, angle)

    base_dir = "./build/figs/experimental"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    plt.figure(figsize=(10, 6))
    plotData(time, f, label=name, title=f"Grafica experimental {name}")
    plt.savefig(f"{base_dir}/experimental_{name}.png")


print("Experimental analysis")
objeto = ['anillo1', 'anillo2', 'cosoMetal1', 'cosoMetal2']
for obj in objeto:
    pendulumAnalysis(obj)
    print(f"Done with {obj}")

# plt.show()
print("All done")
