# cook your dish here
for _ in range(int(input())):
    s = input()
    while(s.count("abc") != 0):
        s = s.replace("abc", "")
    print(s)
