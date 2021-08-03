pas = input()
count = int(input())
words = [input() for i in range(count)]

if pas in words:
    print("YES")
else:
    f1 = False
    f2 = False
    for word in words:
        if pas[0] == word[1]:
            f1 = True
        if pas[1] == word[0]:
            f2 = True
    if f1 and f2:
        print("YES")
    else:
        print("NO")
