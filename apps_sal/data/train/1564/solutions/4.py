t = eval(input())
while t:
    s = input()
    country = []
    for i in range(len(s) - 1):
        temp = s[i] + s[i + 1]
        country += [temp]
    country = set(country)
    print(len(country))
    t -= 1
