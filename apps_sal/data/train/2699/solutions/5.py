nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def number2words(n):
    if n < 20:
        return nums[n]
    if n < 100:
        nn = (n - 20) % 10
        return '%s%s' % (tens[int((n - 20) / 10)], '-' + nums[nn] if nn else '')
    if n < 1000:
        nh = int(n / 100)
        nt = n % 100
        return ('%s hundred %s' % (number2words(nh), number2words(nt) if nt else '')).strip()
    nto = int(n / 1000)
    nh = n % 1000
    return ('%s thousand %s' % (number2words(nto), number2words(nh) if nh else '')).strip()
