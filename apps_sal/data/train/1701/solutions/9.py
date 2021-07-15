class Machine(object):
    
    def __init__(self, cpu: CPU):
        self.cpu = cpu
    
    def execute(self, instr:str):
        # Your code here!
        ins_lst = instr.split(' ')

        # stack operations
        if ins_lst[0] == 'push':
            if ins_lst[1].isdigit():
                self.cpu.write_stack(int(ins_lst[1]))
            else:
                self.cpu.write_stack(self.cpu.read_reg(ins_lst[1]))

        elif ins_lst[0] == 'pop':
            value = self.cpu.pop_stack()
            if len(ins_lst) > 1:
                self.cpu.write_reg(ins_lst[1], value)

        elif ins_lst[0] == 'pushr':
            for reg in ['a', 'b', 'c', 'd']:
                self.cpu.write_stack(self.cpu.read_reg(reg))
            
        elif ins_lst[0] == 'pushrr':
            for reg in ['d', 'c', 'b', 'a']:
                self.cpu.write_stack(self.cpu.read_reg(reg))

        elif ins_lst[0] == 'popr':
            for reg in ['d', 'c', 'b', 'a']:
                self.cpu.write_reg(reg, self.cpu.pop_stack())

        elif ins_lst[0] == 'poprr':
            for reg in ['a', 'b', 'c', 'd']:
                self.cpu.write_reg(reg, self.cpu.pop_stack())


        # misc operations
        elif ins_lst[0] == 'mov':
            ins_lst[1] = ins_lst[1][:-1]
            value = 0
            if ins_lst[1].isdigit():
                value = int(ins_lst[1])
            else:
                value = self.cpu.read_reg(ins_lst[1])
            self.cpu.write_reg(ins_lst[2], value)
            

        # arithmtic operations
        else:
            #varients
            if len(ins_lst[0]) == 4 or (len(ins_lst[0])==3 and ins_lst[0][:2] == 'or'): 
                self.cpu.write_stack(self.cpu.read_reg(ins_lst[0][-1]))
                ins_lst[0] = ins_lst[0][:-1]

            num, target_reg = 0, 'a'
            # find number of vals to pop
            if ins_lst[1][-1] == ',':
                ins_lst[1] = ins_lst[1][:-1]
            if ins_lst[1].isdigit():
                num = int(ins_lst[1])
            else:
                num = self.cpu.read_reg(ins_lst[1])
            # find write back register
            if len(ins_lst) > 2:
                target_reg = ins_lst[2] 

            # exec instruction
            exe_func = lambda x, y: x
            if ins_lst[0] == 'add':
                exe_func = lambda x, y: x+y
                
            elif ins_lst[0] == 'sub':
                exe_func = lambda x, y: x-y

            elif ins_lst[0] == 'mul':
                exe_func = lambda x, y: x*y

            elif ins_lst[0] == 'div':
                exe_func = lambda x, y: x//y

            elif ins_lst[0] == 'and':
                exe_func = lambda x, y: x&y

            elif ins_lst[0] == 'or':
                exe_func = lambda x, y: x|y

            elif ins_lst[0] == 'xor':
                exe_func = lambda x, y: x^y

            result = self.cpu.pop_stack()
            for _ in range(num-1):
                result = exe_func(result, self.cpu.pop_stack())
            self.cpu.write_reg(target_reg, result)

