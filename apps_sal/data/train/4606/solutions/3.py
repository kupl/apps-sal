import re
def valid_romans(arr):
    return [num for num in arr if num and re.match(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', num)]
