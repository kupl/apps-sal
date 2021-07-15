

for _ in range(int(input())): #test_cases
    n=input()
    a=n[::-1]  #reverse and store
    k = 0 ;
    for i in a:  #loop through to remove zeroes at the beginning
        if i =='0': #delete the character from the string
            k += 1 ;
        else:   #exit as soon as a non zero number is found :)
            break
        
    print(a[k:])
