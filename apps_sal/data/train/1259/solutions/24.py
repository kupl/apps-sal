# cook your dish here
for j in range(int(input())):
    count = 0
    l, r = map(int, input().split())
    for i in range(l, r + 1, 1):
        a = str(i)
        if a[-1] == "2" or a[-1] == "3" or a[-1] == "9":
            count += 1
    print(count)
