close_compare=lambda a, b, margin=0: 0 if abs(a-b)<=margin else -1 if a<b else 1
