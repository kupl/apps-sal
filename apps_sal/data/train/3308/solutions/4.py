def parity_bit(binary):
     
      
      return  ' '.join(map(lambda bits : 'error' if bits.count('1')%2 !=0  else bits[:-1] ,binary.split()))
