def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = grid.copy()
    grid_size = len(grid)

    for i in range(grid_size): # Iterate over all rows
        for j in range(grid_size): # Iterate over all columns
            if grid[i, j] == 1: # If the current cell is a tree
                burning_neighbor = False
                # Define relative coordinates for orthogonal neighbors (up, down, left, right)
                neighbor_coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for di, dj in neighbor_coords:
                    ni, nj = i + di, j + dj # Neighbor coordinates

                    # Check if neighbor is within grid bounds
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        if grid[ni, nj] == 2: # If neighbor is burning
                            burning_neighbor = True
                            break # No need to check other neighbors if one is burning

                if burning_neighbor:
                    update_grid[i, j] = 2 # Set the current cell to burning

    return update_grid
