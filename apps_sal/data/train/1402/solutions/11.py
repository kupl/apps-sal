from sys import stdin, stdout
for i in range(int(stdin.readline())):
    stra = int(stdin.readline(), 2)
    strb = int(stdin.readline(), 2)
    count = 0
    while strb != 0:
        (stra, strb) = [stra ^ strb, (stra & strb) * 2]
        count += 1
    print(count)
