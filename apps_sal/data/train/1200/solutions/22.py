for _ in range(int(input())):
    s1 = input()
    f = 0
    for i in range(0, len(s1), 2):
        if s1[i] == s1[i + 1]:
            f = 1
    print('yes') if f == 0 else print('no')
