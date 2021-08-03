
def order_weight(strng):
    # split " " into list
    # iterate over word, iterate over character
    # each word has total, total += int(char)
    lis = strng.split(" ")
    c = []
    for word in lis:
        weight = 0
        for num in word:
            weight += int(num)
        x = {}
        x['number'] = word
        x['weight'] = weight
        c.append(x)
        # print(c)
    # sort list of dict by value
    c.sort(key=lambda x: x['number'])
    c.sort(key=lambda x: x['weight'])
    # iterate through c and return number of each object
    return ' '.join(x['number'] for x in c)
    print(order_weight(strng))
