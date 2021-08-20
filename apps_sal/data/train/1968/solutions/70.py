def is_parent(f1, f2):
    f1 = f1.split('/')
    f2 = f2.split('/')
    if len(f1) > len(f2):
        return False
    for (a, b) in zip(f1, f2):
        if a != b:
            return False
    return True


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        ans = []
        for f in folder:
            if not ans or not is_parent(ans[-1], f):
                ans.append(f)
        return ans
