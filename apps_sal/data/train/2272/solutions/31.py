N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
Bit_num = max(A[-1], B[-1]).bit_length()


def derive(i, A, B):
    pow_2_i = pow(2, i)
    a = [x % pow_2_i for x in A]
    b = [x % pow_2_i for x in B]
    a.sort()
    b.sort()
    ans = 0
    th1 = pow_2_i + pow_2_i // 2
    ib = N - 1
    for ia in range(N):
        a_now = a[ia]
        while ib >= 0 and a_now + b[ib] >= th1:
            ib -= 1
        ans += N - 1 - ib
    th2 = pow_2_i
    ib = N - 1
    for ia in range(N):
        a_now = a[ia]
        while ib >= 0 and a_now + b[ib] >= th2:
            ib -= 1
        ans -= N - 1 - ib
    th3 = pow_2_i // 2
    ib = N - 1
    for ia in range(N):
        a_now = a[ia]
        while ib >= 0 and a_now + b[ib] >= th3:
            ib -= 1
        ans -= N - 1 - ib
    return ans % 2 == 1


ans = 0
for i in range(Bit_num + 1, 0, -1):
    ans += int(derive(i, A, B))
    ans *= 2
print(ans // 2)
