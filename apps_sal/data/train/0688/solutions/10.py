n = int(input())
for i in range(n):
    s = input()
    if s.count("10") + s.count("01") > 2:
        print("non-uniform")
    else:
        print("uniform")
