def interpreter(s):
    memory,pointer,output = [0],0,[]
    for i in s:
        if 0<=pointer<len(memory):
            if i == "+" : memory[pointer] += 1    
            if i == "-" : memory[pointer] += -1   
            if i == '*' : output.append(chr(memory[pointer]%256))
            if i == "!" : memory.append(0)
            if i == '/' : memory[pointer] = 0
            if i == '>' : pointer += 1
            if i == "<" : pointer -= 1
    return "".join(output) or '\x00'
