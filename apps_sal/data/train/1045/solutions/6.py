# cook your dish here
M = 10**9 + 7
for _ in range(int(input())):
    s = input()
    c = ""
    d = [ord("a"), ord("e"), ord("i"), ord("o"), ord("u")]
    for i in s:
        if ord(i) in d:
            c += "0"
        elif 97 <= ord(i) <= 122:
            c += "1"
    print(int(c, 2) % M)
