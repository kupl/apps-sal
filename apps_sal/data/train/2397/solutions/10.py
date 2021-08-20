def main():
    for t in range(int(input())):
        (n, m) = map(int, input().split())
        l = []
        for i in range(n):
            l.append(int(input(), 2))
        l.sort()
        median = (2 ** m - n - 1) // 2
        for i in l:
            if i <= median:
                median += 1
        while median in l:
            median += 1
        ans = bin(median)[2:]
        temp = ''
        for i in range(len(ans), m):
            temp += '0'
        print(temp + ans)


main()
