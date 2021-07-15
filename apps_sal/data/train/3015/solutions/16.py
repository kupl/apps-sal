def get_issuer(n):
    n=str(n)
    if n[:2] in ['34','37'] and len(n)==15:
        return 'AMEX'
    elif n[:4]=='6011' and len(n)==16:
        return 'Discover'
    elif n[:2] in ['51','52','53','54','55'] and len(n)==16:
         return 'Mastercard'
    elif n[0]=='4'and len(n) in [13,16]:
         return 'VISA'
    else:
        return 'Unknown'
  # code your solution here

