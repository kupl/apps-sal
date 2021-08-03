import sys

result = []
n = int(sys.stdin.readline())
for i in range(0, n):
    sys.stdin.readline()
    original = [int(numero) for numero in sys.stdin.readline().strip().split()]
    l = list(set(original))
    l.sort()
    repeats = 0
    number = l[0]
    for j in l:
        c = original.count(j)
        if c > repeats:
            repeats = c
            number = j
    result.append(str(number) + " " + str(repeats))
sys.stdout.write("\n".join(result))
