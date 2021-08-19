try:
    T = int(input())
    for tc in range(T):
        (a, b) = list(map(int, input().split(' ')))
        ans = a + b
        print(ans)
except:
    print('s')
