def find_multiples(a,number):
    
    my_primes = []
      
    for i in range(a, number+1):
       
        if i % a == 0:
            my_primes.append(i)
    return my_primes                      
        
            
      

