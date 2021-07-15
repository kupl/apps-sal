def total_bill(s):
    s = s.replace(" ","")
    return 2 * (len(s)-len(s)//5)
