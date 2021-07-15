def histogram(values, bin_width):
    return [sum([values.count(i + j) for i in range(bin_width)]) for j in range(max(values) + 1) if j % bin_width == 0] if values else []
