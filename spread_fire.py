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
    """Update the forest grid based on fire spreading rules."""
    update_grid = grid.copy()
    grid_size = len(grid)

    for i in range(grid_size - 1):
        for j in range(grid_size - 1):
            if grid[i,j] == 1:
                neighbors = [grid[i - 1,j], grid[i + 1,j], grid[i,j - 1], grid[i,j + 1]]
                if 2 in neighbors:
                    update_grid[i,j] = 2

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

