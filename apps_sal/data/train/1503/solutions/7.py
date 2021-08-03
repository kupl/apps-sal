# cook your dish here
try:
    for _ in range(int(input())):
        l, b = map(int, input().split())
        area = l * b
        while(b):
            l, b = b, l % b
        print(int((area / (l * l))))
except:
    pass
