n, m = list(map(int, input().split()))
set_x = {1, n}
set_y = {1, n}
set_total = {x for x in range(1, n + 1)}

for i in range(0, m):
    x, y = list(map(int, input().split()))
    set_x.add(x)
    set_y.add(y)

result = 0
avai_x = set_total - set_x
avai_y = set_total - set_y
result = len(avai_x) + len(avai_y)
if (n & 1) == 1 and ((n >> 1) + 1) in avai_y and ((n >> 1) + 1) in avai_x:
    result -= 1

print(result)




