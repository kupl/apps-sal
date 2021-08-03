def printPattern(n):
    k = 0
    for i in range(1, n + 1):
        k += i
        j = 1
        l = k
        inc = i
        while (i + j - 1) % n:
            print(l, end=' ')
            l = l + inc
            inc += 1
            j += 1
        while j <= n:
            print(l, end=' ')
            inc -= 1
            l = l + inc
            j += 1
        print()


for tc in range(int(input())):
    n = int(input())
    printPattern(n)
