t = int(input())
while t > 0:
    (n, k) = map(int, input().split())
    q = [int(x) for x in input().split()]
    carry = 0
    for i in range(n):
        if q[i] + carry >= k:
            carry = q[i] + carry - k
        else:
            print(i + 1)
            break
    if carry > 0 and k != 0:
        rem = carry // k + 1 + n
        print(rem)
    elif carry == 0:
        print(n + 1)
    t -= 1
