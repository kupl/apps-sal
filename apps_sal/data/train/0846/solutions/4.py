k, a, b = map(int, input().split())
if (b-a) <= 2: print(k+1)
else:
    count = a
    k = k-(a-1)
    count += (b-a)*(k>>1)
    count += k&1
    print(count)
