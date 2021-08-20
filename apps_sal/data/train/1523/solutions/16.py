n = int(input())
l = list(map(int, input().split()))
if n <= 2:
    print(sum(l))
else:
    ml = [l[0], l[0] + l[1], max(l[0] + l[1], l[1] + l[2], l[0] + l[2])]
    for i in range(3, n):
        new = max(ml[i - 1], l[i] + ml[i - 2], l[i] + l[i - 1] + ml[i - 3])
        ml.append(new)
    print(ml[-1])
