t = int(input())
for tc in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    w, f = list(map(int, input().split()))
    a.sort()
    if(w < f):
        print("Not Possible")
        continue
    sum = 0
    grm = 0
    for i in range(0, f):
        sum = sum + a[i]
        grm = grm + 1

    if(grm < w):
        sum = sum + (w - grm) * a[0]
    print(sum)
