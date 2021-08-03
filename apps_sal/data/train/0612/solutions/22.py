# cook your dish here
t = int(input())
while t > 0:
    s = input()
    n = len(s)
    c = s.find('101', 0, n) + s.find('010', 0, n)
    if c == -2:
        print('Bad')
    else:
        print('Good')
    t = t - 1
