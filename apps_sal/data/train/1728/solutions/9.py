KEYS = ["Right", "Left", "Down", "Up"]
DIRS = [6, 4, 2, 8]
KEYS_DIR = {6: "Right", 4: "Left", 2: "Down", 8: "Up"}
KEYS_DIR_REV = {"Right": 6, "Left": 4, "Down": 2, "Up": 8}
MOVE = [(1, 0), (-1, 0), (0, -1), (0, 1)]
firstTime = False


class PlayerMovement:

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.pressedList = []

    def update(self):
        savedDirection = self.direction
        savedLen = len(self.pressedList)
        i = 0
        firstTime = False
        while i < 4:
            Dir = KEYS_DIR_REV[KEYS[i]]
            Key = KEYS_DIR[DIRS[i]]
            if Input.get_state(Dir):
                if Key not in self.pressedList:
                    self.pressedList.append(Key)
                    self.direction = KEYS_DIR_REV[Key]
                    firstTime = True
            else:
                if Key in self.pressedList:
                    if self.pressedList[-1] == Key:
                        del self.pressedList[-1]
                        if len(self.pressedList) > 0:
                            self.direction = KEYS_DIR_REV[self.pressedList[-1]]
                            firstTime = True
                    else:
                        del self.pressedList[self.pressedList.index(Key)]
            i += 1
        if len(self.pressedList) > 0 and firstTime == False:
            index = KEYS.index(self.pressedList[-1])
            self.position = Tile(self.position.x + MOVE[index][0], self.position.y + MOVE[index][1])
        if savedLen > 0:
            check = 0
            for D in DIRS:
                if Input.get_state(D):
                    check = 1
                    break
            if check == 0:
                self.direction = savedDirection
