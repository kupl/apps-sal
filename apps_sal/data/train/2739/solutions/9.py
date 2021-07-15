def cube_odd(arr):
    ar =  sum([ el **3 for el in arr if type(el) == int and el %2 !=0]) 
    return ar if [el for el in arr if type(el) != int]==[] else None
