s = 0
ele =  1
n = int(input())
l =[0] *(n+2)
a =[0] *(n+2)
ans =[0]* n;
for x in range(n):
    inp = list(map(int,input().strip().split()))
    if inp[0] == 1:
        s += inp[1] * inp[2];
        a[inp[1] - 1] += inp[2]
    elif inp[0] == 2:
        s += inp[1]
        l[ele] = inp[1]
        ele += 1;
    else:
        ele -= 1
        s -= l[ele] + a[ele]
        a[ele -1 ] += a[ele]
        a[ele] = 0
    ans[x] =str( s / ele)
print("\n".join(ans))

