# cook your dish here

n, k = list(map(int, input().split()))

heights = [0 for i in range(n)]

for height in range(n):
    heights[height] = int(input())

heights.sort()

decorated_trees = heights[:k]

height_differences = decorated_trees[-1] - decorated_trees[0]

for i in range(n - k + 1):
    decorated_trees = heights[i:i + k]
    height_differences = min(height_differences, decorated_trees[-1] - decorated_trees[0])
    # print(heights, decorated_trees, height_differences)

print(height_differences)
