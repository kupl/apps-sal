def __starting_point():
 TC = int(input())
 for _ in range(TC):
  ROWS, COLS = list(map(int, input().strip().split()))
  print(f"{ROWS + COLS - 1}.000000")
__starting_point()
