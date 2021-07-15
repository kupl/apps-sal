import collections
def mp():  return map(int,input().split())
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)
def listring(l): return ' '.join([str(x) for x in l])
def ptlist(l): print(' '.join([str(x) for x in l]))

n = it()
p = lt()
a = lt()
b = lt()
m = it()
c = lt()

shirt = list(zip(p,a,b))
shirt.sort()
pointer = [-1,0,0,0]
l = []
for i in range(m):
    cl = c[i]
    while pointer[cl] < n and (shirt[pointer[cl]] == None or cl not in shirt[pointer[cl]][1:]):
        pointer[cl] += 1
    if pointer[cl] == n:
        l.append(-1)
    else:
        l.append(shirt[pointer[cl]][0])
        shirt[pointer[cl]] = None
ptlist(l)
