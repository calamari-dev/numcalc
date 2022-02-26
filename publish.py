from pathlib import Path
import subprocess

filedir = Path(__file__).parent

for fig in filedir.glob("chapter/**/*.py"):
    print("running ./chapter/**/" + fig.name + " ...")
    subprocess.run(["pipenv", "run", str(fig)])


subprocess.run("llmk")
