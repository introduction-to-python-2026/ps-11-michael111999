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
    Spreads fire using vectorized NumPy operations.
    Matches the logic where fire (2) stays fire and spreads to trees (1).
    """
    # Create a mask of where the fire currently is
    is_burning = (grid == 2)
    
    # Shift the burning mask to find neighbors of burning cells
    # This checks Up, Down, Left, and Right (Orthogonal)
    north = np.roll(is_burning, -1, axis=0); north[-1, :] = False
    south = np.roll(is_burning, 1, axis=0);  south[0, :] = False
    east = np.roll(is_burning, -1, axis=1);  east[:, -1] = False
    west = np.roll(is_burning, 1, axis=1);   west[:, 0] = False
    
    # A tree catches fire if it is a tree (1) AND has a burning neighbor
    neighbors_burning = north | south | east | west
    new_fire = (grid == 1) & neighbors_burning
    
    # Apply changes: Trees that caught fire become 2
    res_grid = grid.copy()
    res_grid[new_fire] = 2
    
    return res_grid
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

