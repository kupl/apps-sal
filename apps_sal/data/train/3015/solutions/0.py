def get_issuer(number):
    s = str(number)
    return ("AMEX"       if len(s)==15 and s[:2] in ("34","37") else
            "Discover"   if len(s)==16 and s.startswith("6011") else
            "Mastercard" if len(s)==16 and s[0]=="5" and s[1] in "12345" else
            "VISA"       if len(s) in [13,16] and s[0]=='4' else
            "Unknown")
