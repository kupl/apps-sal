class Solution:
  def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
    array, table = sorted(zip(keyName, keyTime), key=lambda item: item[1]), {}
    for i, (name, time) in enumerate(array):
      table.setdefault(name, []).append(self.convertTime(time))
      
    result = []
    for name, times in table.items():
      for i in range(2, len(times)):
        if times[i] - times[i-2] <= 60:
          result.append(name)
          break
    return sorted(result)
  
  def convertTime(self, time):
    parts = time.split(\":\")
    return int(parts[0]) * 60 + int(parts[1])
