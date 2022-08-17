import subprocess


def start():
    subprocess.call(["poetry", "run", "python", "app.py"])
