def printrev(start):
    for s in range(start, ord('a') - 1, -1):
        print(chr(s), end='')


testcase = int(input())
while testcase:
    k = int(input())
    if k > 25:
        rem = k % 25
        quo = k // 25
        if rem != 0:
            printrev(97 + rem)
        for _ in range(quo):
            printrev(ord('z'))
        print()
    else:
        printrev(97 + k)
        print()
    testcase -= 1
