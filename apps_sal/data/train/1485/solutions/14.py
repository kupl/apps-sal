for _ in range(int(input())):
    n = int(input())
    left = 0
    right = 0
    Dict = {}
    for i in range(n):
        s = input()
        curr_left = s[0:n // 2].count("1")
        curr_right = s[n // 2:n].count("1")
        left += curr_left
        right += curr_right
        Dict[i] = curr_left - curr_right
    ans = abs(left - right)
    org_ans = left - right

    for i in range(n):
        ans = min(ans, abs(org_ans - 2 * Dict[i]))
    print(ans)
