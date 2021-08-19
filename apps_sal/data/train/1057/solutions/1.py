k = int(input())
for char in range(k):
    num = int(input())
    if '4' not in str(num):
        x = len(str(num)) + 1
        print('4' * x)
    elif num % 2 == 0:
        print(num + 3)
    else:
        num = str(num)
        for i in range(len(num) - 1, -1, -1):
            if num[i] == '4':
                index = i
                break
        q = int(index)
        l = num[0:q]
        what = len(num) - (index + 1)
        print(l + '7' + '4' * what)
