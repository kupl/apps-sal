def am_i_wilson(n): return n in (5, 13, 563)

# def am_i_wilson(n):
#    if n < 2:
#        return False
#    elif n == 2:
#        return True
#    else:
#        if n%2 != 0:
#            for i in range(3,int(n**0.5)+1,2):   # only odd numbers
#                if n%i==0:
#                    return False
#            print (n)
#            print ("not feck")
#            return True
#        else:
#            for i in range(2,n):
#                if n%i==0:
#                    print (n)
#                    print ("feck")
#                    return False
#            print (n)
#            print ("not feck")
#            return True
