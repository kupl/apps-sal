class Machine:
    """Class which is taught to use a specific function based on responses."""

    def __init__(self):
        """Create a dictionary which has the possivle command options as entries and they all point towards a 
        specific function to use."""
        self.lambdas = ACTIONS()
        self.commands = dict.fromkeys([x for x in range(len(self.lambdas))], 0)
        self.last_command = None

    def command(self, cmd, num):
        """Calculates number with the function the cmd in the won dictionary currently points to.

        :param cmd: used to reference which function to use
        :param num: which should be calculated
        :returns: calculated value
        """
        cmd = cmd % len(self.lambdas)  # This was very annoying, since it is done in the sample tests but not in the random tests
        self.last_command = cmd
        return self.lambdas[self.commands[cmd]](num)

    def response(self, res):
        """Changes the function used for a specific cmd number if the machine got a negative response for his last command.
        """
        if not res:
            self.commands[self.last_command] += 1 % len(self.lambdas)
