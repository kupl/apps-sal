from re import findall
max_consec_zeros=lambda n: ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen"][max([0]+[len(e) for e in findall(r"0+",bin(int(n))[2:])])]
