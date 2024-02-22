import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Jacobi metode for numerisk løsning av laplaces ligning
def jacobi_iteration_dynamic(old_grid, new_grid, time_step):
    size = len(old_grid)
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            #lagt til for å gjøre det til en dynamisk animasjon, ved hjelp av min kjære venn chat GPT:)
            dynamic_term = 0.1 * np.sin(0.1 * i + 0.1 * j + time_step)
            new_grid[i, j] = 0.25 * (old_grid[i - 1, j] + old_grid[i + 1, j] + old_grid[i, j - 1] + old_grid[i, j + 1]) + dynamic_term

# Function to animate the 3D solution with dynamic changes, litt hjelp fra Chat CPT her og. 
def animate_3d_solution_dynamic(grid, iterations, delay):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    def update(frame):
        nonlocal grid
        ax.clear()
        ax.plot_surface(X, Y, grid, cmap='viridis')
        ax.set_title(f"Iteration: {frame + 1}")

        jacobi_iteration_dynamic(grid, grid, frame)

    ani = animation.FuncAnimation(fig, update, frames=iterations, interval=delay)
    plt.show()

# Setter størrelse på grid
size = 30

# Lager grid for 3d plot
X, Y = np.meshgrid(np.arange(size), np.arange(size))

# Initialiserer grid og legger inn betingelser
old_grid = np.zeros((size, size))
new_grid = np.copy(old_grid)

# Set setter randkrav, kan endres og teste med forskjellige krav.
old_grid[:, 0] = 0
old_grid[:, -1] = 0
old_grid[0, :] = 0
old_grid[-1, :] = 0

# Startpunkt med startverdi
old_grid[1:-1, 1:-1] = 1.0

# antall iterasjoner
iterations = 100

# Animate the 3D solution with dynamic changes and a delay of 100 milliseconds between frames, chattern;)
animate_3d_solution_dynamic(old_grid, iterations, 100)
