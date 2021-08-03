# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    a = s.split(":")
    x = float(a[0])
    y = float(a[1])
    # z=x*60+y
    if x >= 12:
        x -= 12
    deg_min = (y * 30) / 5
    deg_hour = (x * 30 + deg_min / 12)
    # print(deg_min,deg_hour)
    ans = min(abs(deg_min - deg_hour), 360 - abs(deg_min - deg_hour))
    print('{:g}'.format(ans), "degree")
