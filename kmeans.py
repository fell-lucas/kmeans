from arquivos import *
from random import randint
from math import sqrt
from time import process_time

start = process_time()
a = readtable("data/dataset.txt")
k = 6

membros = []
centroids = []
for x in range(0, k):
  centroids.append([0.0,0.0]) # x, y
  membros.append(0)

def dist(p1, p2):
  d = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
  return d

for i in a:
  i.append(randint(0, k - 1))
  membros[i[2]] = membros[i[2]] + 1

for step in range(0, 1000):
  for i, x in enumerate(a):
    centroids[x[2]][0] += x[0]
    centroids[x[2]][1] += x[1]

  for i in range(0, k):
    centroids[i][0] /= membros[i]
    centroids[i][1] /= membros[i]

  for point in a:
    near = dist(point, centroids[point[2]])
    for i, c in enumerate(centroids):
      newnear = dist(point, c)
      if(newnear < near):
        near = newnear
        point[2] = i

print(process_time() - start)

a.sort(key = lambda a: a[2])
open("data/clusters.txt", "w").close()
f1 = open("data/clusters.txt", "a")
for i, line in enumerate(a):
  if(i == 0):
    f1.write(str(line[0]) + " " + str(line[1]) + "\n")
    continue
  elif (a[i][2] != a[i-1][2]):
    f1.write("\n\n")
    f1.write(str(line[0]) + " " + str(line[1]) + "\n")
    continue
  f1.write(str(line[0]) + " " + str(line[1]) + "\n")
f1.close()


xC = []
yC = []
open("data/centroids.txt", "w").close()
f2 = open("data/centroids.txt", "a")
for i, c in enumerate(centroids):
  xC.append(c[0])
  yC.append(c[1])
  f2.write(str(c[0]) + " " + str(c[1]) + "\n\n\n")
f2.close()

plot(column(a, 0), column(a, 1), 'g+')
plot(xC, yC, 'ro')
show()