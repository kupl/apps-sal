def delete_digit(n):
    return max([int(''.join([ch for (index, ch) in enumerate(str(n)) if index != str(n).index(i)])) for i in str(n)])
