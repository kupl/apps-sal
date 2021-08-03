import sys
input()
a = list(map(int, input().split()))
b = sorted(a)
for i in a:
    sys.stdout.write(str(b[b.index(i) - 1]))
    sys.stdout.write(" ")
sys.stdout.write("\n")
