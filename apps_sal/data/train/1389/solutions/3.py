bad_char = ["'", '.', ',', ';', ':']
intial = []
for _ in range(int(input())):
    intial.append(input().split(' '))
for line in reversed(intial):
    for i in reversed(line):
        if i.isalpha():
            print(i, end=' ')
        else:
            for j in bad_char:
                i = i.replace(j, '')
            print(i, end=' ')
    print(end='\n')
