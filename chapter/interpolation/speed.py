from pathlib import PurePath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

filedir = PurePath(__file__).parent
styledir = filedir.parents[1] / "./style"

plt.style.use(str(styledir / "./base.mplstyle"))
mpl.use("pgf")
mpl.rc("pgf", preamble="\\usepackage{" + (styledir / "./matplotlib").as_posix() + "}")

x = np.linspace(0, 1, 300)

plt.figure()
plt.plot(x, x**2, label=r"$x^2$")
plt.plot(x, np.exp(x) - 1, label=r"$\symrm{e}^x-1$")
plt.legend()
plt.savefig(str(filedir / "./speed.pdf"))
