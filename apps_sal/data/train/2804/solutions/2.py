class Chaos(object):
    pass


class Nature(Chaos):

    def buildTree(self, luck):
        n = luck
        tree = ""

        for i in range(1, n + 1):
            # leafs grow in the i'th layer
            temp_layer = Leafs.get_leaf(self)
            for j in range(0, i - 1):
                temp_layer += ' '
                temp_layer += Leafs.get_leaf(self)

            tree += ' ' * (n - i) + temp_layer + "\n"

        # grows from roots to upper branches
        for i in range(n // 3):
            if i == n // 3 - 1:
                tree += ' ' * (n - 1) + Trunk.pieceOfTrunk(self)
                break
            tree += ' ' * (n - 1) + Trunk.pieceOfTrunk(self) + "\n"

        return tree


class Leafs(Nature):
    """Arguments: Tell leaf types as string,
       Receive A(one) leaf as string."""

    def __init__(self, leaftypes):
        self.leaftypes = leaftypes
        self.nextleaf = 0

    def get_leaf(self):
        """Returns the next leaf as singleton string"""
        # increase nextleaf
        self.nextleaf += 1
        # leaft, abbreviation for leaftypes
        leaft = self.leaftypes
        # return the value before increment
        return leaft[(self.nextleaf - 1) % len(leaft)]


class Trunk(Nature):
    def pieceOfTrunk(self):
        return "|"


def custom_christmas_tree(chars, n):
    yaprak = Leafs(chars)
    life = Nature.buildTree(yaprak, n)
    return life
