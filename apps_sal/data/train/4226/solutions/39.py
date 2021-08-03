def remove_smallest(numbers):
    lowest = 0
    check = {}
    check2 = []

    if len(numbers) > 1:
        for i in numbers:
            check[i] = []
            for a in numbers:
                if i < a:
                    check[i].append('lower')
                else:
                    check[i].append('higher')

        for i in numbers:
            check[f'{i} count'] = 0
            for a in numbers:
                if check[i].count('lower') > check[a].count('lower'):
                    check[f'{i} count'] += 1

        for i in numbers:
            check2.append(check[f'{i} count'])
        new_list = []
        for index, elem in enumerate(numbers):
            if index == check2.index(max(check2)):
                continue
            new_list.append(elem)

        return new_list

    else:
        return []
