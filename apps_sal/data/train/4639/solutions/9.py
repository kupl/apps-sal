power_of_two = lambda x: True if sum(int(i) for i in bin(x) if i.isdigit())==1 else False
