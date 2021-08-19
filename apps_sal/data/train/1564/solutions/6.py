t = int(input())
while t:
    a = []
    string = list(input())
    for i in range(len(string) - 1):
        a.append(str(string[i]) + str(string[i + 1]))
    a = set(a)
    print(len(a))
    t -= 1
