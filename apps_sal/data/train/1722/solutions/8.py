class Machine:
    def __init__(self):
        self.cmd = dict()

    def command(self, cmd, num):
        self.last_cmd = cmd
        if cmd in self.cmd:
            return _actions[self.cmd[cmd]](num)
        else:
            self.cmd[cmd] = 0
        return _actions[self.cmd[cmd]](num)

    def response(self, res):
        if res == False:
            self.cmd[self.last_cmd] += 1
