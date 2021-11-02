import os


path = os.getcwd()

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
      if file.find("main.py") == -1: # change commmitwalker
        files.append(os.path.join(r, file))

print(files)

filter = ['mmm']


for f in files:
  with open(f, 'r+') as sc:
    lines = sc.readlines()
    for numb in range(len(lines)):
      line = lines[numb]
      for i in filter:
        if line.find(i) != -1:
          print(f'ERROR: {i} detected at line {numb} in {f}')
          raise RuntimeError("Scan Failed")

print("Commit clean! Enjoy your day!")