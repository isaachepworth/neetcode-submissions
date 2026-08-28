class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        island_count = 0
    
        def markislands(r, c):
            # making sure r or c is not out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or grid[r][c] == "x":
                return
            
            grid[r][c] = "x"  #changes "1" to "x" so i know what has been found while still seeing an island when printed later.
            
            markislands(r + 1, c) # Down
            markislands(r - 1, c) # Up
            markislands(r, c + 1) # Right
            markislands(r, c - 1) # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    markislands(r, c)
                    
        return island_count