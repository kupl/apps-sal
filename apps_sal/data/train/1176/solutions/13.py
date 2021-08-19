from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    cond = True
    n = len(s)
    state = 1
    for i in range(n):
        #print("Start", state)
        if s[i] == '0':
            if state != 1 or state != 5:
                state += 1
            elif state == 5:
                state -= 4
        else:
            if state != 2:
                state = 2
        #print("End", state)
    if state == 5:
        print("YES")
    else:
        print("NO")
