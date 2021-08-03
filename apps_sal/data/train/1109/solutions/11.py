for __ in range(eval(input())):
    n = eval(input())
    k = n**0.5
    if int(k) * int(k) == n:
        print("YES")
    else:
        print("NO")
