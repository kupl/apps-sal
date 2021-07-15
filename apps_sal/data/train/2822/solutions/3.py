numbers = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def name_that_number(x):
    if x < 20:
        return numbers[x]
    a, b = divmod(x - 20, 10)
    if b:
        return '{} {}'.format(tens[a], numbers[b])
    return tens[a]     
