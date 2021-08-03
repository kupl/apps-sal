def mix_fruit(arr):
    Regular = ['banana', 'orange', 'apple', 'lemon', 'grapes']
    Special = ['avocado', 'strawberry', 'mango']
    cost = []
    for fruit in arr:
        fruit = fruit.lower()
        if fruit in Regular:
            cost.append(5)
        elif fruit in Special:
            cost.append(7)
        else:
            cost.append(9)
    return round(sum(cost) / len(cost))
