n = int(input())
total, distance, new_first = 0, 0, 0
a = []
answer = []
length = list(map(str, input().split()))
string = "".join(length)
for i in range(len(string)):
    if(string[i] == '1'):
        a.append(i)
        if(total < len(a)):
            total = len(a)
            start = a[len(a) - 1]
    elif(len(a) != 0 and string[i] == '2'):
        if(len(a) == 1):
            if(distance < i - a[len(a) - 1]):
                distance = i - a[len(a) - 1]
                new_first = a[len(a) - 1]
        a.pop()
answer.append(total)
answer.append(' ')
answer.append(start + 1)
answer.append(' ')
answer.append(distance + 1)
answer.append(' ')
answer.append(new_first + 1)
print(''.join(map(str, answer)))
