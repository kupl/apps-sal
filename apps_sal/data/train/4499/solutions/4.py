import math

 
a_vals = [2]


for i in range(2,50000): 
    if i % 3 != 0:
        a_vals.append(1)
    else:
        a_vals.append(int(i/3)*2)
h_vals = [0,1]
for s in a_vals:
    h = s*h_vals[-1] + h_vals[-2]
    h_vals.append(h)



def convergents_of_e(n):
    
    

    
    output = sum([int(x) for x in str(h_vals[n+1])])
    print(output)
    return(output)
    
    


