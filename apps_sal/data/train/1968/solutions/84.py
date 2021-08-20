class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        seen = set()
        for path in folder:
            if not any((path[i] == '/' and path[:i] in seen for i in range(2, len(path)))):
                seen.add(path)
        return seen
