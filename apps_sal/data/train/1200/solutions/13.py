# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    list_of_strings = []
    count = 0
    for i in range(0, len(s), 2):
        list_of_strings.append(s[i:i + 2])
    for i in list_of_strings:
        if(i == 'AB'):
            count += 1
        elif(i == 'BA'):
            count += 1
    k = len(list_of_strings)
    if(count == k):
        print("yes")
    else:
        print("no")
