class family:
    def __init__(self): self.names = {}
    def male(self, n): return self.setsex(n, 'm')
    def female(self, n): return self.setsex(n, 'f')
    def is_male(self, n): return self.names[n]['sex'] == 'm' if n in self.names else False
    def is_female(self, n): return self.names[n]['sex'] == 'f' if n in self.names else False
    def get_parents_of(self, n): return sorted(self.names[n]['childof']) if n in self.names else []
    def get_children_of(self, n): return sorted(self.names[n]['parentof']) if n in self.names else []

    def updatesex(self):
        for n in [n for n in self.names if len(self.names[n]['childof']) == 2]:
            for a, b in [self.names[n]['childof'], self.names[n]['childof'][::-1]]:
                if self.names[a]['sex'] and not self.names[b]['sex']:
                    self.names[b]['sex'] = 'f' if self.names[a]['sex'] == 'm' else 'm'
                    self.updatesex()

    def setsex(self, name, sex):
        if name not in self.names:
            self.names[name] = {'sex': '', 'parentof': [], 'childof': []}
        if not self.names[name]['sex']:
            self.names[name]['sex'] = sex
            self.updatesex()

        return self.names[name]['sex'] == sex

    def set_parent_of(self, c, p):
        # Create child and/or parent if they do not exist
        for n in [c, p]:
            if n not in self.names:
                self.names[n] = {'sex': '', 'parentof': [], 'childof': []}

        if p in self.names[c]['childof']:
            return True
        if c == p or len(self.names[c]['childof']) == 2:
            return False

        # descendants and ancestors
        for tree, direction, name in [(self.names[c]['parentof'], 'parentof', p), (self.names[p]['childof'], 'childof', c)]:
            while tree:
                if name in tree:
                    return False
                tree = [e for d in tree for e in self.names[d][direction]]

        if len(self.names[c]['childof']) == 1:
            old_p, new_sex = self.names[c]['childof'][0], self.names[p]['sex']

            if new_sex + self.names[old_p]['sex'] in ['mm', 'ff']:
                return False

            # Check for clashing parents
            # Get all couple and create a putative sex dictionary S
            couples = {tuple(self.names[n]['childof']) for n in self.names if len(self.names[n]['childof']) > 1} | {tuple((old_p, p))}

            S = {p: new_sex or 'm'}
            while any(parent in S for couple in couples for parent in couple):
                newcouples = []
                for a, b in couples:
                    if a in S or b in S:
                        if b not in S:
                            S[b] = 'f' if S[a] == 'm' else 'm'
                        if a not in S:
                            S[a] = 'f' if S[b] == 'm' else 'm'
                        if S[a] == S[b]:
                            return False
                    else:
                        newcouples.append((a, b))
                couples = newcouples

        self.names[p]['parentof'] += [c]
        self.names[c]['childof'] += [p]
        self.updatesex()
        return True
