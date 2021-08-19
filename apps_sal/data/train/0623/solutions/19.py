# cook your dish here
n = int(input())
x = []
for i in range(n):
    x.append(int(input()))
x = sorted(x)
for i in x:
    print(i)
