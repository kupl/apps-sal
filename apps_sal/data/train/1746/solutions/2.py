only_show_wrong()


def rpg(map: List[List[str]], actions: List[str]) -> Tuple[List[List[str]], int, int, int, List[str]]:
    class Hero:
        def __init__(self, coordy, coordx, pointer):
            self.coordx = coordx
            self.coordy = coordy
            self.health = 3
            self.attack = 1
            self.defence = 1
            self.pointer = pointer
            self.bag = []
            self.kills = 0
            self.lvlupkills = 0

    class Monsters:
        def __init__(self, coordy, coordx, attack, health):
            self.coordx = coordx
            self.coordy = coordy
            self.attack = attack
            self.health = health

    class DemonLord(Monsters):
        pass

    class Merchant:
        def __init__(self, coordy, coordx):
            self.coordx = coordx
            self.coordy = coordy
            self.health = 3

    def initiate(field):
        monstdict = {}
        merchdict = {}
        hero = 0
        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] == "E":
                    monstdict[(y, x)] = Monsters(y, x, 2, 1)
                elif field[y][x] == "D":
                    monstdict[(y, x)] = DemonLord(y, x, 3, 10)
                elif field[y][x] in ("^", ">", "v", "<"):
                    hero = Hero(y, x, field[y][x])
                elif field[y][x] == "M":
                    merchdict[(y, x)] = Merchant(y, x)
        return (monstdict, hero, merchdict)

    def monsters_move(hero, monstdict):
        for i in [(hero.coordy, hero.coordx - 1), (hero.coordy + 1, hero.coordx), (hero.coordy, hero.coordx + 1),
                  (hero.coordy - 1, hero.coordx)]:
            if i in monstdict:
                hero.health -= max(0, monstdict[i].attack - hero.defence)

    def forward_coords(hero):
        pointer = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        coordx = hero.coordx + pointer[hero.pointer][0]
        coordy = hero.coordy + pointer[hero.pointer][1]
        return (coordx, coordy)

    def move_forward(hero, field, monstdict, merchdict):
        monsters_move(hero, monstdict)
        field[hero.coordy][hero.coordx] = " "
        coords = forward_coords(hero)
        hero.coordx = coords[0]
        hero.coordy = coords[1]
        if 0 <= hero.coordy < len(field) and 0 <= hero.coordx < len(field[hero.coordy]) and field[hero.coordy][
                hero.coordx] not in ("D", "E", "M", "
            if field[hero.coordy][hero.coordx] in ("C", "H", "K"):
                hero.bag.append(field[hero.coordy][hero.coordx])
            elif field[hero.coordy][hero.coordx] == "S":
                hero.defence += 1
            elif field[hero.coordy][hero.coordx] == "X":
                hero.attack += 1
            field[hero.coordy][hero.coordx]=hero.pointer
            return True
        else:
            return False

    def change_pointer(hero, field, monstdict, merchdict, pointer):
        monsters_move(hero, monstdict)
        hero.pointer=pointer
        field[hero.coordy][hero.coordx]=pointer
        if hero.health <= 0:
            return False
        return True

    def use_coin(hero, field, monstdict, merchdict):
        monsters_move(hero, monstdict)
        coords=forward_coords(hero)
        x=coords[0]
        y=coords[1]
        if "C" in hero.bag and (y, x) in merchdict and hero.health > 0:
            merchdict[(y, x)].health -= 1
            hero.bag.pop(hero.bag.index("C"))
            if merchdict[(y, x)].health == 0:
                field[y][x]=" "
                del merchdict[(y, x)]
            return True
        return False

    def use_potion(hero, field, monstdict, merchdict):
        if "H" in hero.bag and hero.health != 3:
            hero.health=3
            hero.bag.pop(hero.bag.index("H"))
        else:
            return False
        monsters_move(hero, monstdict)
        return True if hero.health > 0 else False

    def use_key(hero, field, monstdict, merchdict):
        coords=forward_coords(hero)
        x=coords[0]
        y=coords[1]
        monsters_move(hero, monstdict)
        if "K" in hero.bag and 0 <= x < len(field[y]) and 0 <= y < len(field) and field[y][x] in (
                "-", "|") and hero.health > 0:
            field[y][x]=" "
            hero.bag.pop(hero.bag.index("K"))
            return True
        return False

    def attack(hero, field, monstdict, merchdict):
        coords=forward_coords(hero)
        x=coords[0]
        y=coords[1]
        if (y, x) in monstdict:
            monstdict[(y, x)].health -= hero.attack
            if monstdict[(y, x)].health <= 0:
                hero.lvlupkills += 1
                if hero.lvlupkills == 3:
                    hero.attack += 1
                    hero.lvlupkills=0
                hero.kills += 1
                field[y][x]=" "
                del monstdict[(y, x)]
        else:
            return False
        monsters_move(hero, monstdict)
        return True if hero.health > 0 else False

    field=[[str(x) for x in line] for line in map]
    initialize=initiate(field)
    monstdict=initialize[0]
    hero=initialize[1]
    merchdict=initialize[2]

    actionsdict={"F": move_forward, "A": attack, "C": use_coin, "K": use_key, "H": use_potion}
    for i in actions:
        if i in actionsdict:
            flag=actionsdict[i](hero, field, monstdict, merchdict)
        else:
            flag=change_pointer(hero, field, monstdict, merchdict, i)
        if not flag or hero.health <= 0:
            return None
    return (field, hero.health, hero.attack, hero.defence, sorted(hero.bag))
