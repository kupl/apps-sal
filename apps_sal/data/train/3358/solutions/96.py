def correct(string):
    end =''
    for x in string:
        if x =='0':
            end+='O'
        elif x=='5':
            end +='S'
        elif x=='1':
            end += 'I'
        else:
            end +=x
    return end
