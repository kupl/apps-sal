for t in range(int(input())):
    n = int(input())
    l = list(input())
    total = min(l.count('U'), l.count('D')) + min(l.count('L'), l.count('R'))
    print(2 * total)
