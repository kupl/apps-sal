import sys
cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    N = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    freq = [0] * (1001)
    freq[p[0]] += 1
    error = False
    for i in range(1, len(p)):
        if(freq[p[i]] > 0 and p[i - 1] != p[i]):
            error = True
            break
        else:
            freq[p[i]] += 1
    #  print(freq)
    if(error):
        print("NO")
    else:
        ms = []
        error = False
        for q in freq:

            if q in ms and q != 0:
                error = True
                break
            ms.append(q)
        if(error):
            print("NO")
        else:
            print("YES")
