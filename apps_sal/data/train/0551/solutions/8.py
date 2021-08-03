def check(h):
    for n in h:
        if n > 1:
            return "yes"
    return "no"


for _ in range(int(input())):
    s = input()
    h = [0] * 26

    for c in s:
        h[ord(c) - ord('a')] += 1

    print(check(h))
