def change_count(change):
    total = 0
    for i in change.split(' '):
        if i == 'penny':
            total += 0.01
        elif i == 'nickel':
            total += 0.05
        elif i == 'dime':
            total += 0.1
        elif i == 'quarter':
            total += 0.25
        elif i == 'dollar':
            total += 1.0
    return '${:.2f}'.format(total)


print(change_count('dime penny dollar'))
print(change_count('dime penny nickel'))
print(change_count('quarter quarter'))
print(change_count('dollar penny dollar'))
