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

t, h = (np.pi / 3, 0.2)
x = np.linspace(0.7, 1.4, 300)
f = lagrange([t, t + h], [np.sin(t), np.sin(t + h)])
g = lagrange([t - h, t + h], [np.sin(t - h), np.sin(t + h)])

plt.figure()
plt.plot(x, f(x), label="$l_1$")
plt.plot(x, g(x), label="$l_2$")
plt.plot(x, x / 2 + 1 / 4, label="$x/2+1/4$")
plt.plot(x, np.sin(x), label=r"$\sin(x)$")
plt.scatter([t, t + h], [np.sin(t), np.sin(t + h)])
plt.scatter([t - h, t + h], [np.sin(t - h), np.sin(t + h)])
plt.annotate(r"$x=\symrm{\pi}/3$", xy=(t, np.sin(t)), xytext=(0.9, 0.9))
plt.legend()
plt.savefig(str(filedir / "./differentiation.pdf"))
