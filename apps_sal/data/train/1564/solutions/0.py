#import set
t = eval(input())
while(t):
    s = input()
    set1 = set()
    j = 0
    for i in s[:-1]:
        a = s[j:j + 2]
        set1.add(a)
        j = j + 1
    print(str(len(set1)) + '\n')
    t = t - 1
