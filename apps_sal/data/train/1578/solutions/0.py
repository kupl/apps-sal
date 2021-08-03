for _ in range(eval(input())):
    s = input()
    ans = 0
    for i in s:
        if i.isdigit():
            ans += int(i)
    print(ans)
