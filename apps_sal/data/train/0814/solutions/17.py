for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    streaks = []
    curr_streak = 0
    for i in range(n):
        if l[i] == 0:
            curr_streak += 1
        else:
            if curr_streak > 0:
                streaks.append(curr_streak)
            curr_streak = 0
    num_ones = 0
    all_even_f = 1
    for e in streaks:
        if e == 1:
            num_ones += 1
        elif e % 2:
            all_even_f = 0
    if num_ones == 1 and set(streaks) == {1}:
        print('Yes')
        continue
    if all_even_f:
        print('No')
    else:
        print('Yes')
