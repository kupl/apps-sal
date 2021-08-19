dates = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
months = {1: ('january', 31), 2: ('february', 29), 3: ('march', 31), 4: ('april', 30), 5: ('may', 31), 6: ('june', 30), 7: ('july', 31), 8: ('august', 31), 9: ('september', 30), 10: ('october', 31), 11: ('november', 30), 12: ('december', 31)}
for _ in range(int(input())):
    (D, M) = [n for n in input().split()]
    D = int(D)
    M = M.lower()
    M = dates[M]
    days = 183 - (months[M][1] - D)
    M += 1
    if M > 12:
        M -= 12
    D = 0
    while days > months[M][1]:
        days -= months[M][1]
        M += 1
        if M > 12:
            M -= 12
    print(str(days) + ' ' + str(months[M][0]))
