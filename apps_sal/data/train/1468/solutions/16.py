# cook your dish here
t = int(input())
while(t):
    t = t - 1
    hex = list(input())
    dec = 0
    l = len(hex) - 1
    for i in range(len(hex)):
        if(hex[i] not in "ABCDEF"):
            dec = dec + (16**(l - i)) * int(hex[i])
        else:
            if(hex[i] == 'A'):
                dec = dec + (16**(l - i)) * 10
            elif(hex[i] == 'B'):
                dec = dec + (16**(l - i)) * 11
            elif(hex[i] == 'C'):
                dec = dec + (16**(l - i)) * 12
            elif(hex[i] == 'D'):
                dec = dec + (16**(l - i)) * 13
            elif(hex[i] == 'E'):
                dec = dec + (16**(l - i)) * 14
            else:
                dec = dec + (16**(l - i)) * 15
    print(dec)
