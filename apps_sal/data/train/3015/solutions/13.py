def get_issuer(number):
    card = str(number)
    ln = len(card)
    return ('AMEX' if card[:2] in ('34', '37') and ln == 15 else 
            'Discover' if card[:4] == '6011' and ln == 16 else 
            'Mastercard' if '50' < card[:2] < '56' and ln == 16 else
            'VISA' if card[:1] == '4' and ln in (13, 16) else 'Unknown') 
