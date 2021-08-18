from collections import defaultdict


class Solution:

    def add_suffix(self, name, suffix):
        if suffix == 0:
            return name
        name = name + '(' + str(suffix) + ')'
        return name

    def get_prefix_suff_num(self, name):

        if name.rfind('(') != -1:

            prefix_end = name.rfind('(') - 1
            suff = 0
            i = prefix_end + 2
            while ord(name[i]) >= ord('0') and ord(name[i]) <= ord('9'):
                suff = suff * 10 + ord(name[i]) - ord('0')
                i += 1
        else:
            prefix_end = len(name) - 1
            suff = 0
        return name[:prefix_end + 1], suff

    def get_next_suffix(self, suff, name_suffixes, next_map, name):
        while suff in name_suffixes:
            suff += 1
        next_map[name] = suff

    def getFolderNames(self, names: List[str]) -> List[str]:
        next_map = defaultdict(int)
        suffix_map = defaultdict(set)
        ans = []
        for name in names:
            suffix = next_map[name]
            suffix_map[name].add(suffix)
            new = self.add_suffix(name, suffix)
            suffix_map[new].add(0)
            prefix, suff_number = self.get_prefix_suff_num(name)
            if (len(prefix) < len(name) and suff_number != 0) or (len(prefix) == len(name)):
                suffix_map[prefix].add(suff_number)
                self.get_next_suffix(next_map[prefix], suffix_map[prefix], next_map, prefix)
            self.get_next_suffix(suffix, suffix_map[name], next_map, name)
            self.get_next_suffix(next_map[new], suffix_map[new], next_map, new)
            ans.append(new)
        return ans
