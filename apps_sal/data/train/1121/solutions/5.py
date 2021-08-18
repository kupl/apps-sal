try:
    for _ in range(int(input())):
        time = input().split(':')
        hour = int(time[0])
        minute = int(time[1])
        if hour == 0:
            hour = 12
        elif hour > 12:
            hour = hour - 12
        mindeg = minute * 6
        hourdeg = (hour * 30) + (minute / 60) * 30
        x = abs(hourdeg - mindeg)
        if str(x).split('.')[1] == '0':
            if x > 180:
                print(int(360 - x), 'degree')
            else:
                print(int(x), 'degree')
        else:
            if x > 180:
                print(360 - x, 'degree')
            else:
                print(x, 'degree')
except:
    pass
