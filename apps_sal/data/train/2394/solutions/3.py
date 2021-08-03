for i in range(int(input())):
    n = int(input())
    s = input()
    stack = []
    j = 0
    count = 0
    ans = 0
    while j < len(s):
        if count == 0 and s[j] == ')':
            s += ')'
            ans += 1
        elif count >= 0 and s[j] == '(':
            count += 1
        else:
            count -= 1
        j += 1
    print(ans)
