def nthMagicNo(n):
    pow = 1
    answer = 0
    while n:
        if n & 1:
            answer += pow
        n >>= 1
        pow = pow * 6
    return answer


for _ in range(int(input())):
    a = int(input())
    print(nthMagicNo(a))
