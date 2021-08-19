# cook your dish here
t = int(input())
for z in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    s = len(set(arr))
    if((n - s) % 2 == 0):
        print(s)
    else:
        print(s - 1)
