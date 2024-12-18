"""
placing the building is like: N queens
identify the farthest parking spot: 0/1 matrix. The distance of nearest zero for every 1.
TC: (h*w) C(n): C represents combinations, (h*w) for BFS * (h*w) C(n)
"""
from collections import deque


class BuildingPlacement:
    def __init__(self):
        self.result = float("inf")

    # to find the distance
    def bfs(self, grid, H, W):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque()
        visited = [[False for _ in range(W)] for _ in range(H)]

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    q.append((i, j))

        dist = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for d in directions:
                    r = d[0] + curr[0]
                    c = d[1] + curr[1]
                    if 0 <= r < H and c >= 0 and c < W and not visited[r][c]:
                        visited[r][c] = True
                        q.append((r, c))
            dist += 1

        self.result = min(self.result, dist - 1)

    def dfs(self, grid, r, c, H, W, n):

        # base case: when all the buildings are placed
        if n == 0:
            self.bfs(grid, H, W)

        # end of the first row, move to the next row
        if c == W:
            c = 0
            r += 1

        # logic: out of bound is taken care by this
        for i in range(r, H):
            for j in range(c, W):
                grid[i][j] = 0
                self.dfs(grid, r, j + 1, H, W, n - 1)
                # backtrack
                grid[i][j] = -1

    def findMinDistance(self, H, W, n):
        self.result = float("inf")
        grid = [[-1 for _ in range(W)] for _ in range(H)]
        self.dfs(grid, 0, 0, H, W, n)
        return self.result


# Example Usage
if __name__ == "__main__":
    bp = BuildingPlacement()
    H, W, n = 3, 3, 2  # Example input: Grid of size 3x3 with 2 buildings to place
    result = bp.findMinDistance(H, W, n)
    print(f"Minimum farthest distance: {result}")
