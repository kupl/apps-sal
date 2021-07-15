import re

class Pattern:
    def __init__(self, definition, patterns):
        self._name = re.findall("p([0-9]+)", definition)[0]
        self._calls = re.findall("P([0-9]+)", definition)
        patterns[self._name] = self
    
    def simulate(self, patterns, visited, depths, depth=0):
        if self._name in visited:
            depths.append(depth)
            return
            
        if len(self._calls) == 0:
            depths.append(0)
            return
            
        visited.add(self._name)
        for call in self._calls:
            patterns[call].simulate(patterns, visited, depths, depth+1)
        visited.remove(self._name)

def magic_call_depth_number(pattern):
    patterns = {}
    while True:
        match = re.search("p[0-9]+[^q]*q", pattern)
        if match == None:
            break
        (start, end) = match.span()
        pattern = pattern[0:start] + pattern[end:]
        Pattern(match.group(0), patterns)
        
    depths = []
    for e in re.findall("P([0-9]+)", pattern):
        visited = set()
        patterns[e].simulate(patterns, visited, depths)
    
    if len(depths) == 0:
        return [0, 0]
    else:
        return [min(depths), max(depths)]
