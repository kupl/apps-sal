for _ in range(int(input())):
    li = [int(i) for i in list(input())]
    if len(li) != 1 and sum(li) < 9:
        print(9 - sum(li) % 9)
    else:
        print(min(sum(li) % 9, 9 - sum(li) % 9))
