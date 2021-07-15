get_strings=lambda s:','.join(k+':'+s.lower().count(k)*'*'for k in dict.fromkeys(s.lower().replace(' ','')))
