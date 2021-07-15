def greet(name): 
    name3=''
    name1=name[1:len(name)].lower()
    name2=name[0].upper()
    name3+=name2
    name3+=name1
    return ('Hello '+str(name3)+'!')
