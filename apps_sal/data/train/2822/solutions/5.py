names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def name_that_number(x):
    if x < 20:
        return names[x]
    else:
        return tens[int(x / 10) - 2] + ((' ' + names[x % 10]) if x % 10 > 0 else '')
