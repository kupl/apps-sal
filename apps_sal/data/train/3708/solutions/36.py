def hex_to_dec(s):
    s = s[::-1]
    dec=0
    a = [0] * len(s)
    for i in range(len(s)):
        a[i] = 10 if (s[i] =="a" or s[i]=="A") else 11 if (s[i] =="b" or s[i] =="B") else 12 if (s[i] =="c" or s[i] =="C") else 13 if (s[i] =="d" or s[i] =="D") else 14 if (s[i] =="e" or s[i] =="E") else 15 if (s[i] =="f" or s[i] =="F") else int(s[i]) 
        dec = dec + a[i]*16**i
    return dec
