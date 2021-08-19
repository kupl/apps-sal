def printrev(start):
    for s in range(start, ord('a') - 1, -1):
        print(chr(s), end='')


testcase = int(input())
while testcase:
    k = int(input())
    rem = k % 25
    quo = k // 25
    if rem != 0:
        printrev(97 + rem)
    for _ in range(quo):
        printrev(ord('z'))
    print()
    testcase -= 1
