a = int(input())
for i in range(a):
    total = 0
    str1 = input()
    str2 = input()
    str1 = set(str1)
    for a in str1:
        for b in str2:
            if a == b:
                total = total + 1
    print(total)
