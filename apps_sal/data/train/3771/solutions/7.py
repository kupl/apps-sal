def validate_number(s):
    s = s.replace('+44', '0', 1).replace('-', '')
    return 'In with a chance' if s[:2] == '07' and len(s) == 11 and s.isdigit() else 'Plenty more fish in the sea'
