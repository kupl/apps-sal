n = int(input())
u = []
v = []
for i in range(n-1):
    a, b = map(int, input().split())
    u.append(a)
    v.append(b)
 
c = [0] + [int(x) for x in input().split()]
 
e = 0
dic = {}
 
for i in range(1, n+1):
    dic[i] = 0
 
def plus(dic, n):
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
 
for i in range(n-1):
    if c[u[i]] != c[v[i]]:
        e += 1
        dic[u[i]] += 1
        dic[v[i]] += 1
 
for i in range(1, n+1):
    if dic[i] == e:
        print ('YES', i,sep='\n')
        return
 
print ("NO")

