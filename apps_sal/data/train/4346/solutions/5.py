def hidden(num):
    dic = {'6': 'a', '1': 'b', '7': 'd', '4': 'e', '3': 'i', '2': 'l', '9': 'm', '8': 'n', '0': 'o', '5': 't'}
    return ''.join((dic[i] for i in str(num)))
