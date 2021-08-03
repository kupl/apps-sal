class Nest():

    def __init__(self, key, list):
        self.key = key
        self.list = list
        self.chen = 0
        self.temp_list = []
        self.new_list = []

        self.ACT = {
            1: self.__ap_end__,
            0: self.__swich__
        }

        self.OPER = {
            0: lambda a, b: a < b,
            1: lambda a, b: a >= b
        }

    def __ap_end__(self, c_list, element):
        c_list.append(element)

    def __swich__(self, c_list, element):
        if c_list:
            self.__ap_end__(self.new_list, c_list)
        self.temp_list = [element]
        self.chen = not self.chen

    def do_sort(self):
        if not self.list:
            return []
        for e in self.list:
            self.ACT[self.OPER[self.chen](e, self.key)](self.temp_list, e)
        return self.new_list + [self.temp_list]


def group_ints(lst, key=0): return Nest(key, lst).do_sort()
