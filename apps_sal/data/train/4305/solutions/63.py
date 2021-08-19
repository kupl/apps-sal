def order_weight(numbers):
    return ' '.join(sorted(numbers.split(), key=lambda number: (sum((int(num) for num in number)), number)))
