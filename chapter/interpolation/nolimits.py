from pathlib import PurePath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

filedir = PurePath(__file__).parent
styledir = filedir.parents[1] / "./style"

plt.style.use(str(styledir / "./base.mplstyle"))
mpl.use("pgf")
mpl.rc("pgf", preamble="\\usepackage{" + (styledir / "./matplotlib").as_posix() + "}")

x = np.linspace(-1.5, 0, 600)
x = np.power(10, x)

plt.figure()
plt.xscale("log")
plt.plot(x, np.sin(1 / x), label=r"$\sin(1/x)$")
plt.legend()
plt.savefig(str(filedir / "./nolimits.pdf"))
