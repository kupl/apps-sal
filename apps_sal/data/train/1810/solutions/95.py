class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
    
    
        def base_and_suffix(name):
            # decompose and name into it's base and a list of trailing suffixes
            prefix, split, suffix = name.rpartition(\"(\")
            try:
                assert suffix[-1] == \")\"
                suffix = suffix[:-1]
                suffix = int(suffix)
                assert suffix != 0
                return prefix, suffix
            except:
                return name, None

        used_suffixes = dict()

        def unique_suffix(base, suffix):
            if base not in used_suffixes:
                return base, suffix

            next, used = used_suffixes[base]
            if suffix >= next and suffix not in used:
                return base, suffix
            if suffix:
                # we were given an unusable suffix, append a new suffix
                new_base = base + \"(\" + str(suffix) + \")\"
                return unique_suffix(new_base, 0)

            # find first unused integer
            i = next
            while i in used:
                used.remove(i)
                i += 1

            used_suffixes[base] = i+1, used
            return base, i

        def use_suffix(base, suffix):
            if base not in used_suffixes:
                used_suffixes[base] = 0, set([suffix])
                return

            next, used = used_suffixes[base]
            if suffix == next:
                used_suffixes[base] = suffix+1, used
            else:
                used.add(suffix)

        result = []
        for name in names:
            # print(f\"{name}   {base_and_suffix(name)}\")
            base, suffix = base_and_suffix(name)
            suffix = 0 if suffix is None else suffix
            base, suffix = unique_suffix(base, suffix)
            if suffix:
                name = base + \"(\" + str(suffix) + \")\"
                use_suffix(name, 0)
            else:
                name = base
            use_suffix(base, suffix)
            result.append( name )
            # print(f\" {base} used:   {used_suffixes[base]}\")

        return result

