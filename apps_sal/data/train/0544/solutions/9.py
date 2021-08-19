# cook your dish here
map_dict = {'0000': 'a',
            '0001': 'b',
            '0010': 'c',
            '0011': 'd',
            '0100': 'e',
            '0101': 'f',
            '0110': 'g',
            '0111': 'h',
            '1000': 'i',
            '1001': 'j',
            '1010': 'k',
            '1011': 'l',
            '1100': 'm',
            '1101': 'n',
            '1110': 'o',
            '1111': 'p'}


def decode_it(s):
    l = len(s)
    ch_list = []
    for i in range(0, l, 4):
        ind = s[i:i + 4]
        x = map_dict[ind]
        ch_list.append(x)
    return "".join(ch_list)


T = int(input())
while T > 0:
    l = int(input())
    s = input()
    print(decode_it(s))
    T -= 1
