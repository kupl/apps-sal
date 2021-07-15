class EndException(Exception):
    pass

class DoneAccumulatingException(Exception):
    pass

class OutOfFretsException(Exception):
    pass

def get_column(array, index):
    ret = []
    try:
        for line in array:
            ret.append(line[index])
        return ret
    except IndexError:
        raise EndException()
    
    
def add_to_tab(tab, column):
    for i, value in enumerate(column):
        tab[i] += value


def accumulate(accumulate_array, column):
    if set(map(lambda x: str.isnumeric(x), column)) == {False}:
        raise DoneAccumulatingException()
    else:
        for i, value in enumerate(column):
            accumulate_array[i] += value


def adjust_accumulator(accumulator, adjustment):
    
    column_width = 0
    adjusted_values = []
    for item in accumulator:
        item = item.strip('-')
        if str.isnumeric(item):
            new_value = int(item) + adjustment
            if new_value < 0 or new_value > 22:
                raise OutOfFretsException()
            item = str(new_value)
        adjusted_values.append(item)
        if len(item) > column_width:
            column_width = len(item)

    new_accumulator = [x + ('-' * (column_width - len(x))) for x in adjusted_values]
    return new_accumulator

def transpose(amount, tab):

    idx = 0
    new_tab = [''] * 6
    aa = [''] * 6
    while True:
        try:
            column = get_column(tab, idx)
        except EndException:
            break
        
        try:
            accumulate(aa, column)
        except DoneAccumulatingException:
            try:
                aa = adjust_accumulator(aa, amount)
            except OutOfFretsException:
                return "Out of frets!"

            add_to_tab(new_tab, aa)
            add_to_tab(new_tab, column)
            aa = [''] * 6
            
            #print("UPDATED TAB")
            #for item in new_tab:
            #    print(item[-20:])

        idx += 1
        
    return new_tab
