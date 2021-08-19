displays = {
    '0': '012456',
    '1': '25',
    '2': '02346',
    '3': '02356',
    '4': '1235',
    '5': '01356',
    '6': '013456',
    '7': '025',
    '8': '0123456',
    '9': '012356',
    ' ': ''
}
shape = ' 000 |1   2|1   2|1   2| 333 |4   5|4   5|4   5| 666 '.split('|')


def segment_display(n):
    s = str(n).rjust(6, ' ')
    return '\n'.join('|' + ('|'.join(' ' + (''.join(' #'[c in displays[d]] for c in shape[j]) + ' ') for d in s)) + '|' for j in range(9))
