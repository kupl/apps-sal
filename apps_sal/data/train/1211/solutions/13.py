# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    while s.find("abc") != -1:
        s = s.replace("abc","")
    print(s)

