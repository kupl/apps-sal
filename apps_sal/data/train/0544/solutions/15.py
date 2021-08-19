# cook your dish here
def division(x, s):
    l = []
    for i in range(0, s, 4):
        l.append(x[i:i + 4])
    return l


t = int(input())
for i in range(t):
    size = int(input())
    x = input()
    s = division(x, size)
    string = ""
    for i in s:
        sum1 = 0
        for j in range(4):
            sum1 += (2**(3 - j)) * int(i[j])
        sum1 += 97
        string += chr(sum1)
    print(string)
