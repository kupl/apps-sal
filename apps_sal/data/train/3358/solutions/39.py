def correct(string):
    
    li = []



    for i in string:
        li.append(i)
    print(li)

    for i in range(len(li)):
        if li[i] == '0':
            li[i] = 'O'
        elif li[i] == '1':
            li[i] = 'I'
        elif li[i] == '5':
            li[i] = 'S'


    return "".join(li)
            

