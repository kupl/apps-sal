N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

Bit_num = max(A[-1], B[-1]).bit_length()


def derive(i, A, B):  # i桁目を求める
    pow_2_i = pow(2, i)
    a = [x % pow_2_i for x in A]
    b = [x % pow_2_i for x in B]
    a.sort()
    b.sort()
    # print(i,a,b)
    ans = 0

    th1 = pow_2_i + pow_2_i // 2  # 第１区間を足す
    ib = N - 1
    for ia in range(N):
        a_now = a[ia]
        while ib >= 0 and a_now + b[ib] >= th1:
            ib -= 1
        ans += N - 1 - ib
        #print(" ", ia, ib,1)
    th2 = pow_2_i  # 第２区間を引く
    ib = N - 1
    for ia in range(N):
        a_now = a[ia]
        while ib >= 0 and a_now + b[ib] >= th2:
            ib -= 1
        ans -= N - 1 - ib
        #print(" ", ia,ib,2)
    th3 = pow_2_i // 2  # 第３区間を足す
    ib = N - 1
    for ia in range(N):
        a_now = a[ia]
        while ib >= 0 and a_now + b[ib] >= th3:
            ib -= 1
        ans -= N - 1 - ib
        #print(" ", ia,ib,3)
    return ans % 2 == 1  # Xorをとる。1ならTrue


ans = 0
for i in range(Bit_num + 1, 0, -1):
    ans += int(derive(i, A, B))
    # print(i,ans)
    ans *= 2

print((ans // 2))
