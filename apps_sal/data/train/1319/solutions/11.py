n, m = map(int, input().split())

pos = []
num = 0
while num < m:
    i = int(input())
    if i > 0:
        pos.append(i)
    else:
        print(max(pos))
        pos.remove(max(pos))
        num += 1
