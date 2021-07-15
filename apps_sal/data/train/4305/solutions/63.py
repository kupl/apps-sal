order_weight = lambda numbers: ' '.join(sorted(numbers.split(), key=lambda number: (sum(int(num) for num in number), number)))
