from pathlib import PurePath
import numpy as np
from scipy.interpolate import lagrange
import matplotlib as mpl
import matplotlib.pyplot as plt

filedir = PurePath(__file__).parent
styledir = filedir.parents[1] / "./style"

plt.style.use(str(styledir / "./base.mplstyle"))
mpl.use("pgf")
mpl.rc("pgf", preamble="\\usepackage{" + (styledir / "./matplotlib").as_posix() + "}")

x = np.linspace(-1, 1, 300)
plt.figure()
plt.plot(x, 1 / (25 * x**2 + 1), label="$1/(1+25x^2)$")

t = np.cos(np.pi * (2 * np.linspace(1, 9, 9) - 1) / 18)
p = lagrange(t, 1 / (25 * t**2 + 1))
plt.plot(x, p(x), label="$p(x)$")

plt.legend()
plt.savefig(str(filedir / "./chebyshev.pdf"))
