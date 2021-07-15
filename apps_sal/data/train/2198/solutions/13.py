n = int(input())
names = []
for i in range(n):
    prvs_name = input()
    new_name = ''
    while prvs_name != new_name:
        new_name = prvs_name
        prvs_name = prvs_name.replace('oo', 'u')
        prvs_name = prvs_name.replace('kh', 'h')
        prvs_name = prvs_name.replace('ou', 'uo')
    if new_name not in names:
        names.append(new_name)
print(len(names))
