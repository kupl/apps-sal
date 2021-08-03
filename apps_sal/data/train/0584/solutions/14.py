for _ in range(int(input())):
    S = input().strip()
    count = 0
    Sflag = False
    Cflag = False

    for x in S:
        if x == '1':
            Sflag = True
        else:
            Cflag = True

        if Cflag and x == '1':
            break

        if Sflag and x == '0':
            count += 1

    print(count)
