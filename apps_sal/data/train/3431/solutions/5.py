def warn_the_sheep(queue):
    wolf_positon = 0  # memoy for the position of the wolf
    for postion, item in enumerate(queue):  # lets check every sheep
        if item == 'wolf':  # and if it is a wolf
            wolf_positon = postion + 1  # we will save its position in the memory
        if wolf_positon == len(queue):  # if the wolf is last
            return 'Pls go away and stop eating my sheep'  # We beg the wolf. (Hell no!!!).
    # this f'{variable} some text' doesnt work in every python version(Python >= 3.6)
    # {len(queue)-wolf_positon}example: 1,2,3,4,wolf,5,6 len(queue)=7 wolf_pos=5 7-5=2
    return f'Oi! Sheep number {len(queue)-wolf_positon}! You are about to be eaten by a wolf!'
