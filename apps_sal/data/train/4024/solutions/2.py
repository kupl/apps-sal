def special_number(n):
    return ["NOT!!", "Special!!"][max(str(n)) < "6"]
    
    return "Special!!" if max(str(n)) <= "5" else "NOT!!"     # for length comparison

