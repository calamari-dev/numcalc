from pathlib import PurePath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

filedir = PurePath(__file__).parent
styledir = filedir.parents[1] / "./style"

plt.style.use(str(styledir / "./base.mplstyle"))
mpl.use("pgf")
mpl.rc("pgf", preamble="\\usepackage{" + (styledir / "./matplotlib").as_posix() + "}")

x = 0.03 + np.linspace(0, 0.22, 600)

plt.figure()
plt.plot(x, x * np.sin(1 / x), label=r"$x\sin(1/x)$")
plt.plot(x, x, label="$x$")
plt.legend()
plt.savefig(str(filedir / "./asymptotic.pdf"))
