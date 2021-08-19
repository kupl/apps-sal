def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


n = read()
a = input()
b = input()
a_1 = []
for i in range(n):
    if b[i] == '1':
        a_1.append(a[i])
num0 = a.count('0')
num1 = a.count('1')
num0_1 = a_1.count('0')
num1_1 = a_1.count('1')
print(num0 * num1 - num0_1 * num1_1)
