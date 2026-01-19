import numpy as np

def spread_fire(grid):
    """
    Update the forest grid based on standard fire spreading rules.
    0: Empty/Ash
    1: Tree
    2: Burning
    """
    # We must work on a copy to ensure 'simultaneous' updates
    update_grid = grid.copy()
    grid_size = len(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            # Rule: If the cell is currently burning, it becomes ash (0)
            if grid[i, j] == 2:
                update_grid[i, j] = 0
            
            # Rule: If the cell is a tree, check if any neighbor is burning
            elif grid[i, j] == 1:
                # Orthogonal neighbors: Up, Down, Left, Right
                neighbor_coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                
                for di, dj in neighbor_coords:
                    ni, nj = i + di, j + dj
                    
                    # Check boundary conditions
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        if grid[ni, nj] == 2:
                            update_grid[i, j] = 2
                            break # Move to next cell once ignited
                            
    return update_grid
