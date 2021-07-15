def number(a):
    
    lineCount = 1
    lineList = []


    while a:    #Scenario: While the list is not empy... 
        lineList.append( str(lineCount) + ': ' + a.pop(0) )
        lineCount +=1

    return lineList
#end function number

