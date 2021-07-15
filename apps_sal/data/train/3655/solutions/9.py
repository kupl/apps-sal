class House(object):
    roofleft, roofright = '/', '\\'
    wall = '|'
    bottom = '_'
    
    def __init__(self, floors):
        self.floors = floors
        
    def __new__(cls, floors):
        a = super(House, cls).__new__(cls)
        a.__init__(floors)
        return str(a)
        
    @property
    def width(self):
        return self.floors * 2 + 2
        
    @property
    def height(self):
        return self.floors * 2 + 1
        
    @property
    def roofparts(self):
        return list(range(self.floors))
        
    @property
    def gutterparts(self):
        return list(range(max(self.roofparts) + 1, max(self.roofparts) + 2))
        
    @property
    def floorparts(self):
        return list(range(max(self.gutterparts) + 1, self.height - 1))
        
    @property
    def groundparts(self):
        return list(range(self.height -1, self.height))
    
    def genpart(self, index):
        if index in self.roofparts:
            return self.genroof(index, outerfill=" ", innerfill=" ")
        if index in self.gutterparts:
            return self.genroof(index, outerfill="", innerfill="_")
        if index in self.floorparts:
            return self.genfloor(index, outerfill="", innerfill=" ")
        if index in self.groundparts:
            return self.genfloor(index, outerfill="", innerfill="_")
            
    def genroof(self, index, innerfill, outerfill):
        margin = "{:{outerfill}^{width}}".format("", outerfill=outerfill, width=(self.floors - index))
        roofpart = "{margin}{roofleft}{centerfill}{roofright}{margin}".format(
            margin=margin,
            roofleft=self.roofleft,
            roofright=self.roofright,
            centerfill=innerfill * 2 * index)
        return roofpart
        
    def genfloor(self, index, innerfill, outerfill):
        margin = "{outerfill:{innerfill}^{width}}".format(innerfill=innerfill, outerfill=outerfill, width=self.width)
        roofpart = "{wall}{centerfill}{wall}".format(
            wall=self.wall,
            centerfill=innerfill * (self.width - 2))
        return roofpart
            
    def draw(self):
        lines = []
        for index in range(self.height):
            part = self.genpart(index)
            if not part:
                part = "X" * self.width
            lines.append(part)
        return '\n'.join(lines)
    
    def bounding_box(self):
        lines = []
        for row in range(self.height):
            lines.append('X' * self.width)
        return '\n'.join(lines)
        
    @property
    def __name__(self):
        return [objname for objname,oid in list(globals().items()) if id(oid)==id(self)]
        
    def allnames(self):
        results = [n for n, v in list(globals().items()) if v is arg]
        return results[0] if len(results) is 1 else results if results else None
    
    def __repr__(self):
        #return 'House({})'.format(self.floors)
        return repr(self.draw())
        
    def __str__(self):
        return self.draw()
    
    def describe(self):
        return 'a bVectorian era {} story home called "{}" {{ signified as {}, identified as {} }}'.format(self.floors, self.__name__, repr(self), id(self))
        
my_crib = House

def testings():
    commonhouse = House(1)
    middleclasshouse = House(2)
    ritzyhouse = House(3)
    bigscaryhouse = House(4)
    cribs = [commonhouse,middleclasshouse,ritzyhouse,bigscaryhouse]
    for crib in cribs:
        print(crib)
        print(crib.draw())
        print(crib.roofparts, crib.gutterparts, crib.floorparts, crib.groundparts)

