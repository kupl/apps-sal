try:
    for _ in range(int(input())):
        N = int(input())
        odd = False
        li = [0] * N
        if N & 1 == 1:
            odd = True
            N -= 3
        for i in range(0, N, 2):
            li[i] = i + 2
            li[i + 1] = i + 1
        if odd:
            li[N] = N + 2
            li[N + 1] = N + 3
            li[N + 2] = N + 1
        print(*li)
except Exception as e:
    print(e.__class__)
