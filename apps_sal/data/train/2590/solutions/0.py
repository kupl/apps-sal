import numpy
n,m = list(map(int,input().split()))
ar = []
for i in range(n):
    tmp = list(map(int,input().split()))
    ar.append(tmp)
np_ar = numpy.array(ar)
print((numpy.max(numpy.min(np_ar,axis=1))))

