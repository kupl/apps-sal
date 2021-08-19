import re
ls = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen']


def max_consec_zeros(n):
    return ls[max(map(lambda x: len(x), re.findall('0*', bin(int(n))[2:])))]
