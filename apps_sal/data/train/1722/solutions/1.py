class Machine:

    def __init__(self):
        self.action_for_cmd = {}
        self._actions = ACTIONS()

    def command(self, cmd, num):
        self.last_cmd = cmd
        if cmd not in self.action_for_cmd:
            self.action_for_cmd[cmd] = 0
        return self._actions[self.action_for_cmd[cmd]](num)

    def response(self, res):
        if not res:
            self.action_for_cmd[self.last_cmd] += 1
