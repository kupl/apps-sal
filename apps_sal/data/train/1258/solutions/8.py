for i in range(int(input())):
    n = input()
    total = sum(list(map(int, n)))
    if len(n) > 1 and total < 9:
        print(9 - total)
    else:
        print(min(total % 9, 9 - total % 9))
