from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = input().strip()
    cnt = 0

    if a == a[::-1]:
        print(cnt)

    else:
        lst = list(Counter(a).values())
        odds_count = sum([1 for x in lst if x % 2 != 0])
        if odds_count > 1:
            print(odds_count - 1)
        else:
            print(cnt)
