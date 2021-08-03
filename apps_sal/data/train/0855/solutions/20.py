t = int(input())
while(t):
    s = input()
    ar = [str(x) for x in s]
    print(''.join(str(x) for x in ar[::-1]))
    t -= 1
