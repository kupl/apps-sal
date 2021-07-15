d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
     11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
     19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 
     50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 
     90: 'ninety', 0:''}

def number2words(n):   
    s = (htu(n // 1000) + ' thousand ' if n // 1000 else '') + htu(n % 1000)
        
    return ' '.join(s.split()) if s else 'zero'

    
def htu(n):
    h, tu, u = n//100, n % 100, n % 10
    t = (d[tu] if tu in d else d[tu//10*10] + '-' + d[u]).strip('-')
    return d[h] + ' hundred ' + t if h else t
