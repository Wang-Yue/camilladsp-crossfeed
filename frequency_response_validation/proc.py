
axis = []
dict = {}
for p in ["L", "R"]:
  for q in ["DSP", "RME"]:
    for r in ["1","2","3","4","5"]:
      name = q + p + ' ' + r + ".txt"
      f = open(name, 'r')
      c = f.read()
      f.close()
      lines = [a for a in c.split('\n') if len(a) > 0 and a[0].isdigit()]
      data = [float(a.split(' ')[1]) for a in lines]
      axis = [float(a.split(' ')[0]) for a in lines]
      dict[name] = data

for q in ["DSP", "RME"]:
  for r in ["1","2","3","4","5"]:
    name = q + 'R' + ' ' + r + ".txt"
    base = dict[name][-1]
    for p in ["L", "R"]:
      name = q + p + ' ' + r + ".txt"
      dict[name] = [a  - base for a in dict[name]]

f = open('output.txt', 'w')
f.write('frequency ') 
for r in ["1","2","3","4","5"]:
  for p in ["L", "R"]:
    for q in ["DSP", "RME"]:
      name = q + p + '' + r
      f.write(f'{name} ') 
f.write('\n') 
 
for x in range(len(axis)):
  f.write(f"{axis[x]:.3f} ")
  for r in ["1","2","3","4","5"]:
    for p in ["L", "R"]:
      for q in ["DSP", "RME"]:
        name = q + p + ' ' + r + ".txt"
        f.write(f"{dict[name][x]:.3f} ")
  f.write('\n')
f.close()
