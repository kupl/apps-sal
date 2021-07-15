sa=input()
lo=[]
if '0' in sa:
    
    for char in sa:
        lo.append(char)
    for element in lo:
        if element=='0':
            lo.remove(element)
            break
    string=''
    for element in lo:
        string+=element
    print(string)
else:
    print(sa[1:])

