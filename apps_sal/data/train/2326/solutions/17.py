def main():
    n = int(input())
    a = list(enumerate(map(int, input().split())))

    a.sort(key=lambda x: x[1], reverse=True)
    a.append((-1, 0))

    # min_ind = min(a[:i+1])[0]
    min_ind = n
    ans = [0] * n
    for i in range(n):
        ind, value = a[i]
        if ind < min_ind:
            min_ind = ind

        ans[min_ind] += (value - a[i + 1][1]) * (i + 1)

    for i in ans:
        print(i)


main()
