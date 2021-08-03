t = int(input())
for i in range(t):
    s = input()
    lst = []
    for i in set(s):
        lst.append(s.count(i))
    lst.sort()

    if len(lst) < 3 or lst[-1] == lst[-2] + lst[-3]:
        print("Dynamic")
    else:
        print("Not")
