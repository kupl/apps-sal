vowel_start=lambda s:''.join(' '*(x in'aeiou')+x*x.isalnum()for x in s.lower()).strip()
