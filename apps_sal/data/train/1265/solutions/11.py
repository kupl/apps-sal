def cheffun(k):
    return 10 * cheffun(k // 5) + (k % 5) * 2 if k else 0


g = eval(input())
while (g > 0):
    a = eval(input())
    k = a - 1
    print(cheffun(k))
    g = g - 1
