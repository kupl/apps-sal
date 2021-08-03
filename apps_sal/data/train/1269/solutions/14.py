for t in range(int(input())):
    n = int(input())
    length = [int(i)for i in input().split()]
    width = [int(i)for i in input().split()]
    length.sort()
    width.sort()
    s = 0
    for j in range(n):
        s += min(length[j], width[j])
    print(s)
