for tc in range(int(input())):
    N = int(input())
    (a, b) = list(map(int, input().split()))
    pr = []
    for i in range(N - 1):
        (l, r) = list(map(int, input().split()))
        while a != l or b != r:
            if a > l:
                a -= 1
                pr.append('L-')
            elif a + 1 < b and a < l:
                a += 1
                pr.append('L+')
            elif b < r:
                b += 1
                pr.append('R+')
            elif b - 1 > a and b > r:
                b -= 1
                pr.append('R-')
    print(len(pr))
    print(''.join(pr))
