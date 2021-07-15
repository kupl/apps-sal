def max_consec_zeros(n):
    lookup = {0: 'Zero', 1: 'One', 2: 'Two',
              3: 'Three', 4: 'Four', 5: 'Five',
              6: 'Six', 7: 'Seven', 8: 'Eight',
              9: 'Nine', 10: 'Ten', 11: 'Eleven',
              12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
              15: 'Fifteen'}
    return lookup[len(max(bin(int(n))[2:].split('1'), key=len))]
