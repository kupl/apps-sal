# cook your dish here
t = int(input())
inputarr = []
for _ in range(t):
    a = int(input())
    inputarr.append(a)
final = []
for i in inputarr:
    for j in range(i+1):
        n = list(range(i,i-j-1,-1))
        s = " " * (i-j) + ''.join(str(elem) for elem in n)
        final.append(s)
    for j1 in range(i):
        n1 = list(range(i,j1,-1))
        s1 = " " * (j1+1) + ''.join(map(str,n1))
        final.append(s1)
for i in final:
    print(i)
