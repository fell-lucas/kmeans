from arquivos import *
from random import randint
from math import sqrt

a = readtable("data2.dat")
nClusters = 6

membros = []
posCentroides = []
for x in range(0, nClusters):
  posCentroides.append([0.0,0.0]) # x, y
  membros.append(0)

def dist(p1, p2):
  d = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
  return d

for i in a:
  i.append(randint(0, nClusters - 1))
  membros[i[2]] = membros[i[2]] + 1

for step in range(0, 1000):
  for i, x in enumerate(a):
    posCentroides[x[2]][0] += x[0]
    posCentroides[x[2]][1] += x[1]

  for i in range(0, nClusters):
    posCentroides[i][0] /= membros[i]
    posCentroides[i][1] /= membros[i]

  for ponto in a:
    near = dist(ponto, posCentroides[ponto[2]])
    for i, c in enumerate(posCentroides):
      newnear = dist(ponto, c)
      if(newnear < near):
        near = newnear
        ponto[2] = i

xC = []
yC = []
for c in posCentroides:
  xC.append(c[0])
  yC.append(c[1])

plot(column(a, 0), column(a, 1), 'g+')
plot(xC, yC, 'ro')
show()