class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        vis = set()

        def expand(r,c):
            vis.add((r,c))
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            que = deque()
            que.append((r,c))
            while que:
                row,col = que.popleft()
                for dr,dc in dirs:
                    if 0 <= row+dr < rows and 0 <= col+dc < cols:
                        if (row+dr, col+dc) not in vis and grid[row+dr][col+dc] == '1':
                            vis.add((row+dr, col+dc))
                            que.append((row+dr, col+dc)) 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in vis:
                    islands += 1
                    expand(i,j)
        return islands