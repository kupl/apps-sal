class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        atoms = self.helper(formula)
        return ''.join([e + (str(c) if c > 1 else '') for e, c in sorted(atoms.items())])

    def helper(self, formula):
        i = 0
        atoms = {}
        while i < len(formula):
            if formula[i] == '(':
                end = self.end_parens(formula, i)
                atom = self.helper(formula[i + 1:end])
            else:
                end = self.end_element(formula, i)
                atom = {formula[i:end + 1]: 1}

            i = end + 1
            mult = 0
            while i < len(formula) and formula[i].isdigit():
                mult = mult * 10 + int(formula[i])
                i += 1

            if mult == 0:
                mult = 1

            for element, count in atom.items():
                atoms.setdefault(element, 0)
                atoms[element] += count * mult

        return atoms

    def end_element(self, formula, i):
        i += 1
        while i < len(formula) and formula[i].islower():
            i += 1

        return i - 1

    def end_parens(self, formula, start):
        parens = 1
        i = start + 1
        while i < len(formula) and parens != 0:
            if formula[i] in '()':
                parens += 1 if formula[i] == '(' else -1
            i += 1

        return i - 1
