t = int(input())
while t > 0:
    t -= 1
    preplayers = []
    plagplayers = []
    (n, r, x, y) = map(int, input().split(' '))
    if x:
        preplayers = [int(x) for x in input().split(' ')]
    if y:
        plagplayers = [int(x) for x in input().split(' ')]
    final = len(set(plagplayers).union(set(preplayers)))
    allow = n - final
    if allow > r:
        print(r)
    else:
        print(allow)
