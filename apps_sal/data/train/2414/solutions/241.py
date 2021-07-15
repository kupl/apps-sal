class Solution: 
  def countGoodTripletsCase1(self, arr: List[int], a: int, b: int) -> int:
    count = 0
    for j in range(1, len(arr) - 1):
      l = sum(abs(arr[i] - arr[j]) <= a for i in range(0, j))
      r = sum(abs(arr[j] - arr[k]) <= b for k in range(j + 1, len(arr)))
      count += l * r
    return count

  def countGoodTripletsCase2(self, arr: List[int], a: int, b: int, c: int) -> int:
    index = sorted(range(len(arr)), key=lambda k: arr[k])
    count = 0
    for j in range(len(arr) - 1, 0, -1):
      for i in range(j - 1, -1, -1):
        if index[j] == j: break
        index[j], index[i] = index[i], index[j]
      for k in range(j + 2, len(arr)):
        if arr[index[k - 1]] > arr[index[k]]:
          index[k - 1], index[k] = index[k], index[k - 1]

      i_min = next((i for i in range(0, j) if arr[index[i]] >= arr[j] - a), j)
      i_max = next((i for i in range(i_min, j) if arr[index[i]] > arr[j] + a), j)

      ic_min, ic_max = i_min, i_min
      k = next((i for i in range(j + 1, len(arr)) if arr[index[i]] >= arr[j] - b), len(arr))
      while k < len(arr) and arr[index[k]] <= arr[j] + b:
        while ic_min < i_max and arr[index[ic_min]] < arr[index[k]] - c: ic_min += 1
        while ic_max < i_max and arr[index[ic_max]] <= arr[index[k]] + c: ic_max += 1
        count += ic_max - ic_min
        k += 1

    return count

  def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    if c >= a + b:
      return self.countGoodTripletsCase1(arr, a, b)
    else:
      return self.countGoodTripletsCase2(arr, a, b, c)
