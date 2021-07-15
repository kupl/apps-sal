t = int(input())
mod = []
for i in range (0,t):
    a,b = input().split()
    c=int(a)%int(b)
    mod.append(c)
for i in mod:
    print(i)
