import sys
input = sys.stdin.readline
t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    l = input().split()
    li = [int(i) for i in l]
    li.sort()
    li.reverse()
    z = li[k - 1]
    count = 0
    for i in li:
        if(i >= z):
            count += 1
    print(count)
