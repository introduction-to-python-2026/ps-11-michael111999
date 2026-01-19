import numpy as np

# for plots:
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
 def initialize_forest(grid_size=30, p_tree=0.6):
    """Initialize a grid for the forest fire simulation."""
    grid = np.random.rand(grid_size, grid_size)
    grid = np.where(grid < p_tree, 1, 0)
    grid[grid_size // 2][grid_size // 2] = 2
    return grid
    # Set up the grid

def spread_fire(grid):
    """
    Update rules to match the provided test data:
    1. Trees (1) become Burning (2) if an orthogonal neighbor is Burning (2).
    2. Burning cells (2) REMAIN Burning (2).
    """
    # Create a copy so we don't ignite trees and use them to ignite 
    # other trees in the same time step.
    update_grid = grid.copy()
    grid_size = len(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            # Only need to check logic for trees (1)
            if grid[i, j] == 1:
                # Orthogonal neighbors: Up, Down, Left, Right
                neighbor_coords = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                
                for di, dj in neighbor_coords:
                    ni, nj = i + di, j + dj
                    
                    # Boundary check
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        if grid[ni, nj] == 2:
                            update_grid[i, j] = 2
                            break 
                            
    return update_grid
grid_size = 30
p_tree = 0.6  # Probability that a cell contains a tree

grid = initialize_forest(grid_size, p_tree)

# run the simulation
fig, ax = plt.subplots()
for i in range(100):
    update_grid = spread_fire(grid)
    if np.array_equal(update_grid, grid):
        break
    grid = update_grid
    ax.imshow(grid, cmap='YlOrRd', vmin=0, vmax=2)
    ax.set_title(f'Step {i}')
    display(fig)
    clear_output(wait = True)
    plt.pause(0.01)

