def get_issuer(number):
  number = str(number)
  if number[:2] in ["34", "37"] and len(number) == 15: return("AMEX")
  if number[:4] == "6011" and len(number) == 16: return("Discover")
  if number[:2] in ["51", "52", "53", "54", "55"] and len(number) == 16: return("Mastercard")
  if number[0] == "4" and len(number) in [13, 16]: return("VISA")
  return("Unknown")
