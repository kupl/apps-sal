import string
def solve(s):
    string_list=(list(s))
    alphabets=(list(string.ascii_lowercase))
    test=[]
    for i in range(1,len(alphabets)+1):
        test.append(i)
    my_dictionary=dict(zip(alphabets,test))
    vowels="aeiou"
    vowels_list=list(vowels)
    compare_list1=[]
    for i in range(len(string_list)):
        if string_list[i] in my_dictionary and string_list[i] not in vowels:
            l=(my_dictionary[string_list[i]])
            compare_list1.append(l)
        else:
            compare_list1.append("vowels")
            
    z=(compare_list1)
    x = []
    l = len(z)
    previous_element = 0
    count = 0
    if( isinstance(z[0] , int)  == True ):
            count = z[0]    
    elif( z[0] == 'vowels' ):
            previous_element = z[0]           
    for i in range(1,l):
        if( previous_element == 'vowels' ):
                if(count > 0):
                    x.append(count)
                count = 0       
        elif( isinstance( previous_element , int)  == True ):
                count = count + previous_element
        previous_element = z[i]       
    if( isinstance(z[l-1] , int)  == True ):
            count = count + previous_element
            x.append(count)    
    elif( z[l-1] == 'vowels' ):
            x.append(count)       
    print(x) 
    y=max(x)
    return y
        
solve("zodiacs")
