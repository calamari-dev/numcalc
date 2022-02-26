from pathlib import PurePath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

filedir = PurePath(__file__).parent
styledir = filedir.parents[1] / "./style"

plt.style.use(str(styledir / "./base.mplstyle"))
mpl.use("pgf")
mpl.rc("pgf", preamble="\\usepackage{" + (styledir / "./matplotlib").as_posix() + "}")

x = np.linspace(0, 6, 300)

plt.figure()
plt.plot(x, x**2 - 6 * x + 9, label="$f(x)$")
plt.plot(x, -x + 7, label="$g(x)$")
plt.scatter([1, 3, 4], [4, 0, 1])
plt.scatter([1, 5, 4], [6, 2, 3])
plt.legend()
plt.savefig(str(filedir / "./interpolation.pdf"))
