for u in range(int(input())):
    n = int(input())
    s = input()
    r = min(s.count('U'), s.count('D')) * 2 + min(s.count('L'), s.count('R')) * 2
    print(r)
