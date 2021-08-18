t = int(input())
while t:
    n = int(input())
    r1 = input()
    r2 = input()
    r1count = 0
    r2count = 0
    count = 0
    for i in range(n):
        if(r1[i] == "*"):
            r1count += 1
        if(r2[i] == "*"):
            r2count += 1
    if(r1count > 0) and (r2count > 0):
        count = 1
        r1count = 0
        r2count = 0
        i = 0
        while(i < n):
            if(r1[i] == "*"):
                r1count += 1
            if(r2[i] == "*"):
                r2count += 1
            if(r1count > 1) or (r2count > 1):
                count += 1
                r1count = 0
                r2count = 0
                i -= 1
            i += 1
    elif(r1count == 0 and r2count > 0) or (r2count == 0 and r1count > 0):
        count = max(r1count, r2count) - 1
    else:
        count = 0
    print(count)
    t -= 1
