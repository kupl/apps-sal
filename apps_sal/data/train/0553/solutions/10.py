T = int(input())
for tc in range(T):
    p, q, r = map(int, input().split())
    a, b, c = map(int, input().split())
    p_diff = a - p
    q_diff = b - q
    r_diff = c - r
    flag = 0

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    g_c_d = gcd(a, gcd(b, c))

    def factors(x):
        result = []
        i = 2
        while i * i <= x:
            if x % i == 0:
                result.append(i)
                if x // i != i:
                    result.append(x // i)
            i += 1
        return result
    listi = factors(g_c_d)

    try:
        p_rem = a / p
    except:
        p_rem = 1
    try:
        q_rem = b / q
    except:
        q_rem = 1
    try:
        r_rem = c / r
    except:
        r_rem = 1

    if a == p and b == q and c == r:
        print("0")
        flag = 1
        continue
    elif p_rem == q_rem == r_rem != 1:
        print("1")
        flag = 1
        continue
    elif p_diff == q_diff == r_diff:
        print("1")
        flag = 1
        continue
    elif p == a and q == b:
        print("1")
        flag = 1
        continue
    elif p == a and r == c:
        print("1")
        flag = 1
        continue
    elif q == b and r == c:
        print("1")
        continue
    elif p == a:
        if q_diff == r_diff:
            print("1")
            flag = 1
            continue
        elif q_rem == r_rem != 1:
            print("1")
            flag = 1
            continue
        else:
            print("2")
            flag = 1
            continue
    elif q == b:
        if p_diff == r_diff:
            print("1")
            flag = 1
            continue
        elif p_rem == r_rem != 1:
            print("1")
            flag = 1
            continue
        else:
            print("2")
            flag = 1
            continue
    elif r == c:
        if q_diff == p_diff:
            print("1")
            flag = 1
        elif q_rem == p_rem != 1:
            print("1")
            flag = 1
            continue
        else:
            print("2")
            flag = 1
    elif p_diff == 0:
        if q_diff == r_diff:
            print("1")
            flag = 1
            continue
        elif q_rem == r_rem:
            print("1")
            flag = 1
            continue
        else:
            print("2")
            flag = 1
            continue
    elif q_diff == 0:
        if p_diff == r_diff:
            print("1")
            flag = 1
            continue
        elif p_rem == r_rem:
            print("1")
            flag = 1
            continue
        else:
            print("2")
            flag = 1
            continue
    elif r_diff == 0:
        if p_diff == q_diff:
            print("1")
            flag = 1
            continue
        elif p_rem == q_rem:
            print("1")
            flag = 1
            continue
        else:
            print("2")
            flag = 1
            continue
    elif r_diff - p_diff == q_diff:
        print("2")
        continue
    elif r_diff - q_diff == p_diff:
        print("2")
        continue
    elif q_diff - r_diff == p_diff:
        print("2")
        continue
    elif q_diff - p_diff == r_diff:
        print("2")
        continue
    elif p_diff - q_diff == r_diff:
        print("2")
        continue
    elif p_diff - r_diff == q_diff:
        print("2")
        continue

    elif p_diff == q_diff:
        print("2")
        flag = 1
        continue
    elif q_diff == r_diff:
        print("2")
        flag = 1
        continue
    elif p_diff == r_diff:
        print("2")
        flag = 1
        continue
    elif p_rem == q_rem and r_rem != 1:
        print("2")
        flag = 1
        continue
    elif p_rem == r_rem and q_rem != 1:
        print("2")
        flag = 1
        continue
    elif q_rem == r_rem and p_rem != 1:
        print("2")
        flag = 1
        continue
    elif ((a // g_c_d) - p) == ((b // g_c_d) - q) == ((c // g_c_d) - r):
        print("2")
        flag = 1
        continue
    if flag == 0:
        try:
            if (r_diff - b) / q == (r_diff - a) / p:
                print("2")
                flag = 1
                continue
        except:
            if (r_diff - b) / 1 == (r_diff - a) / 1:
                print("2")
                flag = 1
                continue
        try:
            if (q_diff - c) / r == (q_diff - a) / p:
                print("2")
                flag = 1
                continue
        except:
            if (q_diff - c) / 1 == (q_diff - a) / 1:
                print("2")
                flag = 1
                continue
        try:
            if (p_diff - c) / r == (p_diff - b) / q:
                print("2")
                flag = 1
                continue
        except:
            if (p_diff - c) / 1 == (p_diff - b) / 1:
                print("2")
                flag = 1
                continue
        try:
            if (b / r_rem) - q == a - p:
                print("2")
                flag = 1
                continue
        except:
            if (b / 1) - q == a - p:
                print("2")
                flag = 1
                continue
        try:
            if (a / r_rem) - p == b - q:
                print("2")
                flag = 1
                continue
        except:
            if (a / 1) - p == b - q:
                print("2")
                flag = 1
                continue
        try:
            if (b / p_rem) - q == c - r:
                print("2")
                flag = 1
                continue
        except:
            if (b / 1) - q == c - r:
                print("2")
                flag = 1
                continue
        try:
            if (c / p_rem) - r == b - q:
                print("2")
                flag = 1
                continue
        except:
            if (c / 1) - r == b - q:
                print("2")
                flag = 1
                continue
        try:
            if (c / q_rem) - r == a - p:
                print("2")
                flag = 1
                continue
        except:
            if (c / 1) - r == a - p:
                print("2")
                flag = 1
                continue
        try:
            if (a / q_rem) - p == c - r:
                print("2")
                flag = 1
                continue
        except:
            if (a / 1) - p == c - r:
                print("2")
                flag = 1
                continue

    if flag == 0:
        try:
            if (b - (c - r)) / q == p_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (b - (c - r)) / x == p_rem:
                print("2")
                flag = 1
                continue
        try:
            if (b - (a - p)) / q == r_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (b - (a - p)) / x == r_rem:
                print("2")
                flag = 1
                continue

        try:
            if (a - (b - q)) / p == r_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (a - (b - q)) / x == r_rem:
                print("2")
                flag = 1
                continue
        try:
            if (a - (c - r)) / p == q_rem:
                print("2")
                flag = 1
                continue

        except:
            x = 1
            if (a - (c - r)) / x == q_rem:
                print("2")
                flag = 1
                continue
        try:
            if (c - (b - q)) / r == p_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (c - (b - q)) / x == p_rem:
                print("2")
                flag = 1
                continue
        try:
            if (c - (a - p)) / r == q_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (c - (a - p)) / x == q_rem:
                print("2")
                flag = 1
                continue
        try:
            if (b / r_rem) / q == p_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (b / x) / x == p_rem:
                print("2")
                flag = 1
                continue
        try:
            if (a / r_rem) / p == q_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (a / x) / x == q_rem:
                print("2")
                flag = 1
                continue
        try:
            if (b / p_rem) / q == r_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (b / x) / x == r_rem:
                print("2")
                flag = 1
                continue
        try:
            if (c / p_rem) / r == q_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (c / x) / x == q_rem:
                print("2")
                flag = 1
                continue
        try:
            if (a / q_rem) / p == r_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (a / x) / x == r_rem:
                print("2")
                flag = 1
                continue
        try:
            if (c / q_rem) / r == p_rem:
                print("2")
                flag = 1
                continue
        except:
            x = 1
            if (c / x) / x == p_rem:
                print("2")
                flag = 1
                continue

    if flag == 0:
        try:
            if b / (q + (c - r)) == a / (p + (c - r)):
                print("2")
                flag = 1
                continue
        except:
            rem1 = 1
            rem2 = 1
            if b / rem1 == a / rem2:
                print("2")
                flag = 1
                continue

        try:
            if c / (r + (b - q)) == a / (p + (b - q)):
                print("2")
                flag = 1
                continue
        except:
            rem1 = 1
            rem2 = 1
            if c / rem1 == a / rem2:
                print("2")
                flag = 1
                continue

        try:
            if b / (q + (a - p)) == c / (r + (a - p)):
                print("2")
                flag = 1
                continue
        except:
            rem1 = 1
            rem2 = 1
            if b / rem1 == c / rem2:
                print("2")
                flag = 1
                continue

    if flag == 0:
        if(p - q != 0):
            rem = (a - b) / (p - q)
            diff = a - (p * rem)
            if(rem % 1 == 0 and diff % 1 == 0 and (r * rem + diff) == c):
                print("2")
                flag = 1
    if flag == 0:
        if len(listi) > 0:
            for x in listi:
                if ((a // x) - p) == ((b // x) - q) == ((c // x) - r):
                    print("2")
                    flag = 1
    if flag == 0:
        if a - (q_rem * p) == c - (q_rem * r):
            print("2")
            flag = 1
            continue
        elif a - (r_rem * p) == b - (r_rem * q):
            print("2")
            flag = 1
            continue
        elif c - (p_rem * r) == b - (p_rem * q):
            print("2")
            flag = 1
            continue
    if flag == 0:
        print("3")
