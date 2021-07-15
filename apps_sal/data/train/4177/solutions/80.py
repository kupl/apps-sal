def men_from_boys(arr):
    '''this is not the most elegant or concise solution, but it is functional'''
    even_men=[]
    odd_boys=[]
    boys_men=[]
    #make two seperate lists of even and odd numbers
    for number in arr:
        if number%2==0:
            even_men.append(number)
        else:
            odd_boys.append(number)
    #Get rid of the duplicates in each list with sets
    even_men=set(even_men)
    odd_boys=set(odd_boys)
    #Since sets are unordered collection of unique elements, convert them back to lists
    even_men=list(even_men)
    odd_boys=list(odd_boys)
    #Sort the even/odd lists according to ascending/descending order, respectively
    even_men.sort()
    odd_boys.sort(reverse=True)
    #Then combine these two lists into one list, preserving their respective orders
    for number in even_men:
        boys_men.append(number)
    for number in odd_boys:
        boys_men.append(number)
    #Return the final list
    return boys_men
