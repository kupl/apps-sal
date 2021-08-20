t = int(input())
while t:
    t -= 1
    time = input()
    (hrs, mins) = time.split(':')
    (hrs, mins) = (int(hrs), int(mins))
    total_mins = hrs * 60 + mins
    ha = 0.5 * total_mins % 360
    ma = 6 * total_mins % 360
    ans1 = abs(ha - ma)
    ans2 = 360 - ans1
    ans = min(ans1, ans2)
    if not ans % 1:
        ans = int(ans)
    print(ans, 'degree')
