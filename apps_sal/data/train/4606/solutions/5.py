def valid(n):
    if not n:
        return False
    import re
    return re.fullmatch('(M|MM|MMM|MMMM)?'
                        '(C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?'
                        '(X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?'
                        '(I|II|III|IV|V|VI|VII|VIII|IX)?', n)


def valid_romans(arr):
    return [n for n in arr if valid(n)]
