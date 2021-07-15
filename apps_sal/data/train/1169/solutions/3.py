WORDS = {"F":"FRIENDS", "L":"LOVE", "A":"ADORE", "M":"MARRIAGE", "E":"ENEMIES", "S":"SISTER"}
cases = int(input())
for case in range(cases):
    a = input().strip().lower()
    b = input().strip().lower()
    
    i = 0
    while i < len(a):
        k = b.find(a[i])
        
        if k != -1:
            a = a[:i]+a[i+1:]
            b = b[:k]+b[k+1:]
            i -= 1
        i += 1
        
    letters = len(a)+len(b)
    if letters == 0:
        print("SISTER")
        continue
    
    flames = "FLAMES"
    i = 0
    while len(flames) > 1:
        i = (i+letters-1) %len(flames)
        flames = flames[:i]+flames[i+1:]
    print(WORDS[flames])
