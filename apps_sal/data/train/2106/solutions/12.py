chef_sum = 0
ramsay_sum = 0
odds_mids = []
for n in range(int(input())):
    c, *c_list = map(int, input().split())
    if c%2 == 1:
        odds_mids.append(c_list.pop(c//2))
    for index,element in enumerate(c_list):
        if index < len(c_list)/2:
            chef_sum += element
        else:
            ramsay_sum += element
odds_mids.sort(reverse = True)
for index, element in enumerate(odds_mids):
    if index%2 == 0:
        chef_sum += element
    else:
        ramsay_sum += element
print(chef_sum, ramsay_sum)
