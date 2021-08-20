d = {1: 0}
st = 1
prev = 1
while True:
    new = st + st + 1
    d[new] = prev
    prev = new
    st = new
    if st > 2 * 2 ** 30:
        break
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
    else:
        try:
            print(d[n])
        except:
            print(-1)
