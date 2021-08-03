# cook your dish here
def possible(l, n, k):
    pass


def bs(l, n, d):
    i = 1
    j = d
    ans = 1
    while i <= j:
        mid = i + (j - i) // 2
        if possible(l, n, mid):
            ans = mid
            i = mid + 1
        else:
            j = mid - 1
    return ans


t = int(input())
for _ in range(t):
    n, d = list(map(int, input().split()))
    l = list(map(int, input().split()))
    # print(bs(l,n,d))
    # k=[]
    for j in l[::-1]:
        c = d // j
        d = c * j

    print(d)
