testc = int(input())
for i in range(testc):
    a, b, c = input().split()
    A = int(a)
    B = int(b)
    C = int(c)
    lis = list(map(int, input().split()))
    s = sum(lis)
    ans = s // B
    if(ans > C):
        print(C)
    else:
        print(ans)
