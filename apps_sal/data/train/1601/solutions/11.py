# cook your dish here
def R(): return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n, p = R()
    max_no = n - (int(n / 2) + 1)
    # print(max_no)
    if max_no == 0:
        print(p * p * p)
    else:
        ans = (p - max_no)**2 + (p - n) * (p - max_no) + (p - n)**2
        print(ans)
