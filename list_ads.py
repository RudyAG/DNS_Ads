f = open("list.txt", "r")
g = open("listads.txt", "a")
for x in f:
  print(x) 
  x="0.0.0.0 "+x
  print(x)
  g.write(x)
f.close() 
