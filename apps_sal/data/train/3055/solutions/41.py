def sum_str(a, b):
    return str(int(a) + int(b)) if a != "" and b != "" else a if a != "" and b == "" else b if a == "" and b != "" else '0'
