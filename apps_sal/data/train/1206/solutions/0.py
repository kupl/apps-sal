from sys import stdout, stdin
n,m,o = list(map(int, stdin.readline().split()))
n= n+m+o
l=[]
a=[]
for i in range(n):
    b= int(stdin.readline())
    if(b in l and b not in a):
        l.append(b)
        a.append(b)
    elif(b not in l):
        l.append(b)


a.sort()
stdout.write(str(len(a)) + '\n')
stdout.write(''.join([str(id) + '\n' for id in a]))
    

