from itertools import permutations
for _ in range(int(input())):
    a = list(input())
    for i in sorted(set(permutations(a, 2))):
        c = int(i[0]) * 10 + int(i[1])
        if c >= 65 and c < 91:
            print(chr(c), end="")
    print("")
