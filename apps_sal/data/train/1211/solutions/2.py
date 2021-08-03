testcases = int(input())
for i in range(testcases):
    s = input()
    x = s.find("abc")
    while(x != -1):
        s = s.replace("abc", "")
        x = s.find("abc")
    print(s)
