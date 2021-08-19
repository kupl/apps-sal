def __starting_point():
    t = int(input())
    for q in range(t):
        n = int(input())
        l = list(map(int, input().split()))
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if l[i] != l[j]:
                    if l[l[i] - 1] == l[l[j] - 1]:
                        count += 1
                        break
        if count == 0:
            print('Poor Chef')
        else:
            print('Truly Happy')


__starting_point()
