x = input().split(' ')
y = input()
ans = ''
l = 1
for i in x:
    if i != y and sorted(i) == sorted(y):
        ans = ans + str(l)
    l = l + 1
ans += '.'
print('The antidote is found in', ans)
