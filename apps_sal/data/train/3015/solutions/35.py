def get_issuer(number):
    strng=str(number)
    
    if len(strng)==16:
        if strng[0:4] in ['6011']:
            return 'Discover'
        if strng[0:2] in ['51','52','53','54','55']:
            return 'Mastercard'
        if strng[0] in ['4']:
            return 'VISA'
        
    elif len(strng)==15:
        if strng[0:2] in ['34','37']:
            return 'AMEX'
    
    elif len(strng)==13:
        if strng[0] in ['4']:
            return 'VISA'
    
    
    return 'Unknown'
