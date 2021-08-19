n = input()

# print(n)

names = set()

for i in range(0, int(n)):
    s = input()

    while "kh" in s:
        s = s.replace("kh", "h")

    while "u" in s:
        s = s.replace("u", "oo")

    #print("->", s)
    # print(i)
    names.add(s)

print(len(names))
