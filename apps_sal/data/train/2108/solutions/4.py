3

names = input().split()
n = int(input())
for i in range(n):
    print(' '.join(names))
    sep = input().split()
    if names[0] == sep[0]:
        names[0] = sep[1]
    if names[1] == sep[0]:
        names[1] = sep[1]
    
print(' '.join(names))

