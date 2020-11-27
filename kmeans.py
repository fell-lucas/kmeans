from random import randint
from math import sqrt
from time import process_time
from pylab import plot, show

'''
This is an implementation of the k-means clustering algorithm,
in a bidimensional world, for the machine learning course of 
2020/2 in the Universidade Federal do Pampa.

Teacher: Marcelo Resende Thielo
'''

#start timer
start = process_time()
f = open("data/dataset.txt", "r")
lines = f.readlines()
f.close()

a = []
for line in lines:
  data = [float (i) for i in line.split(" ")]
  a.append(data)

#number of clusters
k = 6

#initialize members of a cluster and centroids array
members = []
centroids = []
for x in range(0, k):
  centroids.append([0.0,0.0]) # x, y
  members.append(0)

#euclidian distance function
def dist(p1, p2):
  d = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
  return d

#assign members to clusters randomly
for i in a:
  i.append(randint(0, k - 1))
  members[i[2]] += 1

#kmeans iterative approximation
for step in range(0, 1000):

  #the centroid coordinates is the sum of the coordinates of its members
  for i, x in enumerate(a):
    centroids[x[2]][0] += x[0] #x
    centroids[x[2]][1] += x[1] #y

  #divided by the number of the total members in the cluster
  for i in range(0, k):
    centroids[i][0] /= members[i]
    centroids[i][1] /= members[i]

  #reallocate the individual points from it's previous centroid to the closest one
  for point in a:
    near = dist(point, centroids[point[2]])
    for i, c in enumerate(centroids):
      newnear = dist(point, c)
      if(newnear < near):
        near = newnear
        point[2] = i

print(process_time() - start)

#write the final clusters to files
a.sort(key = lambda a: a[2])
open("data/clusters.txt", "w").close()
f1 = open("data/clusters.txt", "a")
for i, line in enumerate(a):
  if(i == 0):
    f1.write(str(line[0]) + " " + str(line[1]) + "\n")
    continue
  elif (a[i][2] != a[i-1][2]): #separate each cluster by a double line break, gnuplot understands it
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

#get xs and ys to plot
xData = [x[0] for x in a]
yData = [x[1] for x in a]

#plot using matplotlib's pyplot
#if you'd like to use gnuplot, here's an input string you could use:
#plot for [i=0:*] "data/clusters.txt" index i with points pt 7, "data/centroids.txt" with points pt 2 ps 2
plot(xData, yData, 'm+')
plot(xC, yC, 'yo')
show()