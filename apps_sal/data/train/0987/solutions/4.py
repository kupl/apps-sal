import math
for i in range(int(input())):
    (f, db, ta, bs) = map(int, input().split())
    if f / bs < math.sqrt((f + db) * 2 / ta):
        print('Bolt')
    else:
        print('Tiger')
