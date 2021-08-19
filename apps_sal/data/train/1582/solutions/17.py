n = int(input())
s = input()
b = 0
i = 0
j = 0
while i < n - 1:
    j = i + 1
    while j < n:
        if s[i] == s[j]:
            #print("case 1 j",j)
            b += 1
            j += 1
            i += 1
        else:
            #print("case 2 j :",j)
            i = j
            break

print(b)
