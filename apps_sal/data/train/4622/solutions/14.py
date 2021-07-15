double_check=lambda strng: any(x.lower()==strng[i+1].lower() for i,x in enumerate(strng[:-1]))
