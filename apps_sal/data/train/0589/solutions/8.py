def __starting_point():
    for _ in range(int(input())):
        s = input()
        L, count, days = 0, 0, 0
        for c in s:
            if(c == "
                if(count > L):
                    days += 1
                    L=count
                count=0
            else:
                count += 1
        if(count > L):
            days += 1
        print(days)


__starting_point()
