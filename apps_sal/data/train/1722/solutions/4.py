class Machine:

    def __init__(self):
        self.actions = ACTIONS()
        self.command_to_action_map = {}
        self.current_command = 0

    def command(self, cmd, num):
        if not cmd in self.command_to_action_map:
            self.command_to_action_map[cmd] = 0
        self.current_command = cmd
        action_index = self.command_to_action_map[cmd]
        return self.actions[action_index](num)

    def response(self, res):
        if res == False:
            self.command_to_action_map[self.current_command] += 1
            self.command_to_action_map[self.current_command] %= len(self.actions)
