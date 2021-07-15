def interpreter(tape):
    selector = 0
    output = ""
    array = [0]
    commandIndex = 0
    
    while(True):
      command = tape[commandIndex%len(tape)]
      
      if command == '>':
        selector+=1;
        if selector == len(array):
          array.append(0)
      
      if command == '<':
        if selector == 0:
          array = [0] + array  
        else:
          selector-=1;
        
      if command == '+':
        array[selector]+=1;
        if array[selector] == 256:
          array[selector] = 0
      if command == '-':
        array[selector]-=1;
        if array[selector] == -1:
          array[selector] = 255
      if command == '/':
        if array[selector] == 0:
          commandIndex += 1
      if command == '\\':
        if array[selector] != 0:
          commandIndex += 1
      if command == '*':
        output = output + chr(array[selector])
      if command == '&':
        return output        
      commandIndex+=1  
    return output
