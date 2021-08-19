t = int(input())
for i in range(0, t):
    my_int = int(input().strip())
    for xyz in range(1, my_int + 1):
        for abc in range(1, my_int + 1):
            print('{0}{1}'.format(abc, xyz), end='')
        print()
