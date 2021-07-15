from collections import Counter
def numeric_palindrome(*args):
    seen = set()
    products = set()
    for number in args:
        for multiplier in seen.union(products):
            products.add(multiplier*number)
        seen.add(number)

    palindromes = set()
    for number in products:
        occurrences = Counter(str(number))
        repeated= []
        max_single = ''
        for char, count in occurrences.items():
            if count//2 > 0 and char != '0':
                repeated.extend([char]*(count//2))
            if count%2 == 1:
                if max_single < char: max_single = char
        
        half_palindrome = ''
        while repeated:
            maximum = max(repeated)
            half_palindrome += maximum
            repeated.remove(maximum)
        if half_palindrome: half_palindrome += '0'*(occurrences['0']//2)
        palindrome = half_palindrome + max_single + half_palindrome[::-1]
        palindromes.add(int(palindrome))
    return max(palindromes)
