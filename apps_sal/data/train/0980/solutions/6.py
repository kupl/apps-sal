#!/usr/bin/python
def __starting_point():
    t = input()
    t = int(t)
    while(t > 0):
        string = input()
        ip_list = string.split(' ')
        n = int(ip_list[0])
        b = int(ip_list[1])
        m = int(ip_list[2])
        ans = 0
        while(n > 0):
            if n % 2 == 0:
                ans += n / 2 * m
                n -= n / 2
                if n > 0:
                    ans += b
            else:
                ans += (n + 1) / 2 * m
                n = (n - 1) / 2
                if n > 0:
                    ans += b
            m *= 2
        print(ans)
        t -= 1


__starting_point()
