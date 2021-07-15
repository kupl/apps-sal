def find_middle(string):
    if not type(string) == str:
        return -1
    numbers = [int(i) for i in string if i.isdigit()]
    if not numbers:
        return -1
    prod = 1
    for i in numbers:
        prod *= i
    prod_str = str(prod)
    return int(prod_str[(len(prod_str) // 2) - 1:(len(prod_str) // 2) + 1]) if len(prod_str) % 2 == 0 else int(prod_str[len(prod_str)//2])
