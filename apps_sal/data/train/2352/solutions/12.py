s = input()
if s[0:3] == 'ftp':
    s = s.replace('ftp', 'ftp://', 1)
    s = s[0:7] + s[7:].replace('ru', '.ru/', 1)
else:
    s = s.replace('http', 'http://', 1)
    s = s[0:8] + s[8:].replace('ru', '.ru/', 1)
if s[-1] == '/':
    print(s[0:-1])
else:
    print(s)
