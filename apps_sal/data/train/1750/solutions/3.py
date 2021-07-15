mystery=lambda n:n ^ (n >> 1)
mystery_inv=lambda n,i=0,li=[0]:int(''.join(map(str,li)),2) if i==len(bin(n)[2:]) else mystery_inv(n,i+1,li+[int(li[-1])^int(bin(n)[2:][i])])
name_of_mystery=lambda:'Gray code'
