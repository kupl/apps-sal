# cook your dish here
for _ in range(int(input())):
    g = input()
    h = g[::-1]
    if h == g:
        print(1)
    else:
        print(2)
