def get_digits_sum(number):
    return sum([int(sign) for sign in number if sign.isdigit()])
    
def custom_sorting(numbers):
    values = [(get_digits_sum(number), number) for number in numbers]
    return [value[1] for value in sorted(values)]

def order_weight(strng):
    return " ".join(custom_sorting(strng.strip().split(" ")))
