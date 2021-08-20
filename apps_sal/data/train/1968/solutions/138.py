class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        res = []
        files = sorted(folder)
        stack = [files[0]]
        for i in range(1, len(files)):
            if not files[i].startswith(stack[-1] + '/'):
                stack.append(files[i])
        return stack
