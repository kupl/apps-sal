# cook your dish here
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, q = list(map(int, stdin.readline().split()))
    arr = list(map(int, stdin.readline().split()))[:n]
    od = ev = 0
    for i in arr:
        if bin(i).count('1') % 2 == 0:
            ev += 1
        else:
            od += 1
    for _ in range(q):
        p = int(stdin.readline())
        if bin(p).count('1') % 2 == 0:
            stdout.write(str(ev) + " " + str(od) + "\n")
        else:
            stdout.write(str(od) + " " + str(ev) + "\n")
