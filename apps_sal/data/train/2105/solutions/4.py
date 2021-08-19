n = int(input())
if n == 1:
    print(1)
    print(1)
elif n == 2:
    print(1)
    print('1 1')
else:
    print(2)
    ans = []

    def prime(q):
        j = 2
        while j * j <= q:
            if q % j == 0:
                return False
            j += 1
        return True
    for i in range(2, n + 2):
        if prime(i):
            ans.append('1')
        else:
            ans.append('2')
    print(' '.join(ans))
