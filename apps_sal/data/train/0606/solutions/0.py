# cook your dish here
T = int(input())
for i in range(T):
    l = list(map(int, input().split()))
    n, k, m, x = l[0], l[1], l[2], l[3]
    if k == 1:
        if n == m:
            print("yes")
        else:
            print("no")
    elif m % k > 1:
        print("no")
    elif k == 2:
        stack = []
        var = 0
        while m != 0:
            var += m % k
            stack.append(m % k)
            m //= k
        if var > n:
            print("no")
        elif var == n:
            print("yes")
        else:
            for p in range(100):
                for q in range(2, len(stack)):
                    if stack[q - 1] == 0 and stack[q] >= 1:
                        stack[q-1] = 2
                        stack[q] -= 1
                        var += 1
                        if var == n:
                            print("yes")
            if var < n:
                print("no")
    else:
        temp = 0
        rog = 1
        while m != 0:
            if m % k > 2:
                rog = 0
                print("no")
            temp += m % k
            m //= k
        if rog:
            if temp == n:
                print("yes")
            else:
                print("no")


