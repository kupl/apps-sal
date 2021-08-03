def name_that_number(x):
    d = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
         6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    e = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
         12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    if x < 20:
        return e.get(x, None)

    else:
        return d.get(x // 10, '') + (' ' + e.get(x % 10, '') if x % 10 != 0 else '')
