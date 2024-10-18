import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def calculate_in_circle_points(points:list, radius:int):
    in_circle_points = []
    not_in_circle_points = []
    for point in points:
        if point[0]**2 + point[1]**2 <= radius**2:
            in_circle_points.append(point)
        else:
            not_in_circle_points.append(point)

    return in_circle_points, not_in_circle_points

def calculate_random_points(circle_center:tuple, radius:int, points:int):
    max_x = circle_center[0] + radius 
    min_x = circle_center[0] - radius 
    max_y = circle_center[1] + radius 
    min_y = circle_center[1] - radius

    return [(random.uniform(min_x, max_x), random.uniform(min_y, max_y)) for _ in range(points)]

def update(frame, total_points, batch_size, circle_center, radius, all_points, scatter_in, scatter_out, text_pi, text_iter):
    # Generate new batch of points
    new_points = calculate_random_points(circle_center, radius, batch_size)
    all_points.extend(new_points)
    
    # Calculate points inside and outside the circle
    in_circle, not_in_circle = calculate_in_circle_points(all_points, radius)
    
    # Update scatter plots for points inside and outside the circle
    scatter_in.set_offsets(in_circle)
    scatter_out.set_offsets(not_in_circle)
    
    # Estimate π dynamically
    pi_estimation = 4 * (len(in_circle) / len(all_points))
    
    # Update text for π estimation and iteration number
    text_pi.set_text(f'π estimation: {pi_estimation:.6f}')
    text_iter.set_text(f'Iteration: {len(all_points)}')
    
    return scatter_in, scatter_out, text_pi, text_iter

if __name__ == "__main__":
    # Circle properties
    center = (0, 0)
    radius = 1

    # Number of points and animation settings
    total_points = 100000  
    batch_size = 1000  
    
    all_points = []

    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.4)

    # Scatter plots for points inside and outside the circle
    scatter_in = ax.scatter([], [], color='green', s=1)
    scatter_out = ax.scatter([], [], color='red', s=1)
    
    # Dynamic text for π estimation and iteration number
    text_pi = ax.text(-0.9, 1.25, '', fontsize=14, color='blue')
    text_iter = ax.text(-0.9, 1.15, '', fontsize=14, color='blue')
    
    # Set the title with a larger font size
    ax.set_title('Monte Carlo Simulation for π Estimation', fontsize=16, pad=20, color='darkblue')
    
    # Adjust the legend for better visibility
    ax.legend(loc='upper right', fontsize=12, frameon=True)
    
    # Initialize the animation
    ani = animation.FuncAnimation(fig, update, frames=range(total_points // batch_size), 
                                  fargs=(total_points, batch_size, center, radius, all_points, scatter_in, scatter_out, text_pi, text_iter),
                                  interval=50, blit=True)

    # Display the animation
    plt.show()
