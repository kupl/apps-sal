nums = {0: 'Zero', 1: 'One',
        2: 'Two', 3: 'Three',
        4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven',
        8: 'Eight', 9: 'Nine',
        10: 'Ten', 11: 'Eleven',
        12: 'Twelve', 13: 'Thirteen'}


def max_consec_zeros(n):
    return nums[max(map(len, bin(int(n))[2:].split('1')))]
