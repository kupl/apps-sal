to_lover_case=lambda s:''.join('LOVE'[(ord(e.lower())-97)%4]if e.isalpha()else e for e in s)
