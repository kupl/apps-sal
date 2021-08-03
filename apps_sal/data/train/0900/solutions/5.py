from sys import stdin, stdout


def sin():
    return stdin.readline()


def out(s):
    stdout.write(str(s) + "\n")


m = 1000000007
for i in range(int(input())):
    n = int(sin())
    print(((2**n) * 5) % m)
