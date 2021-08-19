def get_order(order):
    (menu, Menu) = (['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke'], ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke'])
    (str, num) = ('', 0)
    (lst, lst2, result) = ([], [], [])
    for letter in order:
        str += letter
        if str in menu:
            lst.append(str)
            str = ''
    for word in lst:
        lst2.append(word.capitalize())
    for counter in range(0, 8):
        for word in lst2:
            if word == Menu[counter]:
                result.append(word)
    return ' '.join(result)
