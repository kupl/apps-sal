def animals(h,l):
    co = (l-2*h)/2   #amount of cows
    ch = h-co        #amount of chickens
    return("No solutions" if co.is_integer() == False else ((h-co,co) if (co<0 or ch<0) == False else "No solutions"))


            
    

