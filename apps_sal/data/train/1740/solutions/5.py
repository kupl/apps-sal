class Family(dict):
    def __init__(self): super().__init__()

    def __getitem__(self, name):
        if name in self:
            return super().__getitem__(name)
        ret = self[name] = Ppl(name)
        return ret

    def __setitem__(self, name, ppl):
        if name in self:
            raise Exception(f"cannot reassign a member of the family: {name}, {ppl}")
        super().__setitem__(name, ppl)

    def female(self, name): return self.male(name, isMale=False)

    def male(self, name, isMale=True):
        who = self[name]
        if who.hasGender() and isMale != who.isMale:
            return False
        who.isMale = isMale
        ok = all(c.updateGenders() for c in who.children)
        if not ok:
            who.isMale = None
        return ok

    def is_male(self, name): p = self[name]; return p.hasGender() and p.isMale
    def is_female(self, name): p = self[name]; return p.hasGender() and not p.isMale
    def get_children_of(self, name): return sorted(p.name for p in self[name].children)
    def get_parents_of(self, name): return sorted(p.name for p in self[name].parents)

    def set_parent_of(self, *childParent):
        c, p = (self[x] for x in childParent)
        return c.set_parent(p)


family = Family


class Ppl:
    def __init__(self, name, isMale=None):
        self.name = name
        self.isMale = isMale
        self.children = []
        self.parents = []

    def __eq__(self, o): return isinstance(o, self.__class__) and o.name == self.name
    def __hash__(self): return hash(self.name)
    def __repr__(self): return f'Ppl({self.name},{self.isMale} ; p={[p.name for p in self.parents]}, c={[p.name for p in self.children]})'
    def hasGender(self): return self.isMale is not None
    def has2Parents(self): return len(self.parents) == 2

    def acyclic(self, target, seens=None):
        if seens is None:
            seens = set()
        if target in seens:
            return False
        if self in seens:
            return True
        return seens.add(self) or all(c.acyclic(target, seens) for c in self.children)

    def set_parent(self, p):
        if p in self.parents:
            return True
        if self.has2Parents() or self == p:
            return False
        self.parents.append(p)
        p.children.append(self)
        if self.acyclic(p) and self.updateGenders():
            return True
        self.parents.pop()
        p.children.pop()
        return False

    def updateGenders(self, seensC=None, tome=()):
        if not self.has2Parents():
            return True
        a, b = self.parents
        if b.hasGender() or b in tome:
            a, b = b, a
        nG = a.hasGender() + b.hasGender()

        if seensC is None:
            seensC, tome = set(), {}
            if not nG:
                tome[a] = 1
                return all(c.updateGenders(seensC, tome) for c in a.children if c not in seensC)
        seensC.add(self)

        if nG == 2:
            return a.isMale ^ b.isMale
        if a in tome and b in tome:
            return tome[a] ^ tome[b]
        if nG == 1:
            b.isMale = not a.isMale
        elif a in tome:
            tome[b] = 1 ^ tome[a]
        isOK = all(c.updateGenders(seensC, tome) for c in b.children if c not in seensC)
        if not isOK and nG == 1:
            b.isMale = None
        return isOK


"""
def logger(f):
    @wraps(f)
    def wrapper(self, *a,**kw):
        print('-------')
        print(f.__name__, a, kw)
        print("\t"+"\n\t".join(map(str,self.values())))
        ret = f(self,*a,**kw)
        x = "\n\t\t".join(map(str,self.values()))
        print(f'***\n{f.__name__} returns: {ret}\nFinal state:\t{x}\n------\n')
        return ret
    return wrapper

from functools import wraps
from inspect import *

for name,f in getmembers(Family, predicate=isfunction):
    if not name.startswith('__'):
        setattr(Family, name, logger(f))
