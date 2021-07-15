def get_issuer(number):
  if len(str(number))==15:
      return 'AMEX' if str(number)[:2] in ['34','37'] else 'Unknown'
  elif len(str(number)) in[13,16]:
      if str(number)[:4]=='6011':
          return 'Discover'
      elif str(number)[:2] in list(map(str,range(51,56))):
          return 'Mastercard'
      elif str(number)[0]=='4':
          return 'VISA'
      else:
          return 'Unknown'
  else:
      return 'Unknown'
