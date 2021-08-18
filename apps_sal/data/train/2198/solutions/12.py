n = input()


names = set()

for i in range(0, int(n)):
    s = input()

    while "kh" in s:
        s = s.replace("kh", "h")

    while "u" in s:
        s = s.replace("u", "oo")

    names.add(s)

print(len(names))
