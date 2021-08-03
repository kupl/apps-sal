t = int(input())
for i in range(t):
    h = input()
    hr = h[::-1]
    if h == hr:
        print(1)
    else:
        print(2)
