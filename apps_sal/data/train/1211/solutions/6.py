t1 = int(input())
for i in range(t1):
    s1 = input()
    while("abc" in s1):
        s1 = s1.replace("abc", "")
    print(s1)
