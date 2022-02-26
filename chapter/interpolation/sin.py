from pathlib import PurePath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

filedir = PurePath(__file__).parent
styledir = filedir.parents[1] / "./style"

plt.style.use(str(styledir / "./base.mplstyle"))
mpl.use("pgf")
mpl.rc("pgf", preamble="\\usepackage{" + (styledir / "./matplotlib").as_posix() + "}")

x = np.linspace(-75, 100, 300)

plt.figure()
plt.plot(x, np.sin(np.pi * x / 180), label=r"$\sin(\symrm{\pi}x/180)$")
plt.plot(x, -0.00005 * x**2 + 0.01825 * x - 0.0039, label="$p(x)$")
plt.legend()
plt.savefig(str(filedir / "./sin.pdf"))
