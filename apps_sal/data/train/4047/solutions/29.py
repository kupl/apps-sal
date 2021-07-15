
d = {
          'A': '@',
          'B' : '8',
          'C' : '(',
          'D' : 'D',
          'E' : '3',
          'F' : 'F',
          'G' : '6',
          'H' : '#',
          'I' : '!',
          'J': 'J',
          'K' : 'K',
          'L' : '1',
          'M' : 'M',
          'N' : 'N',
          'O' : '0',
          'P' : 'P',
          'Q' : 'Q',
          'R' : 'R',
          'S' : '$',
          'T' : '7',
          'U' : 'U',
          'V' : 'V',
          'W' : 'W',
          'X' : 'X',
          'Y' : 'Y',
          'Z' : '2'
}

def to_leet_speak(str):

    a = []
    
    for i in range(len(str)):
        
        if str[i] in list(d.keys()):
            
            a.append(d[str[i]])
              
        else:
            
            a.append(str[i])
                                   
    p = "".join(a)

    return p


