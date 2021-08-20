def extract(s):
    codes = {}
    for i in range(len(s) - 1):
        cc = s[i:i + 2]
        if cc not in codes:
            codes[cc] = True
    return len(codes)


t = int(input())
for i in range(t):
    print(extract(input()))
