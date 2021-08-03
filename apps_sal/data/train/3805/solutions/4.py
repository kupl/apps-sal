def histogram(values, bin_width):
    k = []
    end = max(values) if values else -1
    bin = [i for i in range(bin_width, end + bin_width + 1, bin_width)]
    for i in bin:
        count = 0
        for val in values:
            if i - bin_width <= val < i:
                count += 1
        k += [count]
    return k
