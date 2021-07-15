display_board=lambda b,w:f"\n{'-'*(4*w-1)}\n".join(["|".join(" "+c+" " for c in b[i:i+w]) for i in range(0,len(b)-1,w)])

