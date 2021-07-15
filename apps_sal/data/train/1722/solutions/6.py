class Machine:
    def __init__(self):
        _actions = ACTIONS()
        self.actions ={}
    def command(self, cmd, num):
        self.cmd=cmd
        self.actions[cmd] = self.actions.get(cmd,ACTIONS())
        return self.actions[cmd][0](num)
    def response(self,res):
        if not res:
            self.actions[self.cmd]=self.actions[self.cmd][1:]
