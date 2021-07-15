class Machine:
    def __init__(self):
        self.cmd = dict()
        self._actions = [lambda x: x + 1, lambda x: 0, lambda x: x / 2, lambda x: x * 100, lambda x: x % 2]

    def command(self, cmd, num):
        self.last_cmd = cmd
        if cmd  in self.cmd:
            return self._actions[self.cmd[cmd]](num)
        else:
            self.cmd[cmd] = 0
        return self._actions[self.cmd[cmd]](num)

    def response(self,res):
        if res == False:
            self.cmd[self.last_cmd] += 1
