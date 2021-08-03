from re import findall
def max_consec_zeros(n): return ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen"][max([0] + [len(e) for e in findall(r"0+", bin(int(n))[2:])])]
