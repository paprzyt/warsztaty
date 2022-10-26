from pathlib import Path

filename = 'paths.py'
mypath = Path.cwd() / Path(filename)
if mypath.exists:
    print("File exists")
    print(mypath.name)
    print(mypath.parent)
    print(mypath.suffix)