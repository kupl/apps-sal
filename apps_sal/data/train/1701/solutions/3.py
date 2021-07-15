from operator import add, sub, mul, floordiv, or_, xor, and_
import re

class Machine(object):

    OP_FUNCS = {"add": add, "sub": sub, "mul": mul, "div": floordiv, "or": or_, "xor": xor, "and": and_}
    REG_LST, REG_REVLST = "abcd","dcba"
    REG_SET = set(REG_LST)
    
    def __init__(self, cpu): self.cpu = cpu
    
    def execute(self, instr):
        cmds = re.split(r'[ ,]+', instr)
        
        if   cmds[0] == "pop":        self.cpu.pop_stack() if len(cmds) == 1 else self.pop(cmds[1])
        elif cmds[0] == "popr":       self.loop(self.REG_REVLST, self.pop)
        elif cmds[0] == "poprr":      self.loop(self.REG_LST, self.pop)
        elif cmds[0] == "push":       self.push(cmds[1])
        elif cmds[0] == "pushr":      self.loop(self.REG_LST, self.push)
        elif cmds[0] == "pushrr":     self.loop(self.REG_REVLST, self.push)
        elif cmds[0] == "mov":        self.mov(cmds[1], "a" if len(cmds) == 2 else cmds[2])
        else:                         self.operation(cmds[0], cmds[1], "a" if len(cmds) == 2 else cmds[2])

    def push(self, regint):           self.cpu.write_stack( self.cpu.read_reg(regint) if regint in "abcd" else int(regint))
    def pop(self, reg):               self.cpu.write_reg(reg, self.cpu.pop_stack())
    def mov(self, val, reg):          self.cpu.write_reg(reg, int(val))
    
    def loop(self, regLst, func):
        for reg in regLst: func(reg)
    
    def operation(self, opType, regint, reg):
        nToPop = self.cpu.read_reg(regint) if regint in "abcd" else int(regint)
        
        if opType[-1] == "a":
            opType = opType[:-1]
            self.push("a")
        
        result = self.cpu.pop_stack()
        for x in range(nToPop-1):
            result = self.OP_FUNCS[opType](result, self.cpu.pop_stack())
        self.cpu.write_reg(reg, result)
