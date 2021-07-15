def switch_it_up(number):
    num_in_words = {
        0 : 'Zero',
        1 : 'One',
        2 : 'Two',
        3 : 'Three',
        4 : 'Four',
        5 : 'Five',
        6 : 'Six',
        7 : 'Seven',
        8 : 'Eight',
        9 : 'Nine'
    }
    return num_in_words.get(number,"enter any number from 0 through 9")
