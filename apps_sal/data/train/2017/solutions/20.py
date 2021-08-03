n = int(input())
n = n * 2
x = [int(i) for i in input().split()]
swap = 0
while 0 < n:
    temp = x[1:].index(x[0])
    swap = swap + temp
    x.remove(x[0])
    x.remove(x[temp])
    n = n - 2
print(swap)
