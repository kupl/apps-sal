class Solution:
  def getFolderNames(self, names: List[str]) -> List[str]:
    d, ans = {}, []
    for x in names:
      if x in d:
        i = d[x]
        while f\"{x}({i})\" in d:
          i += 1
        d[x] = i + 1
        d[f\"{x}({i})\"] = 1
        ans.append(f\"{x}({i})\")
      else:
        d[x] = 1
        ans.append(x)
    return ans
