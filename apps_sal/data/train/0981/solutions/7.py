NAME = "P5"
try:
    inFile = open(NAME + ".txt")
except:
    pass


def read():
    try:
        return inFile.readline().strip()
    except:
        return input().strip()


cases = int(read())
for _ in range(cases):
    n = int(read())
    skill = list(map(int, read().split()))
    skill.sort()
    best = 1000000000
    for i in range(1, len(skill)):
        best = min(best, skill[i] - skill[i - 1])
    print(best)
