import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----- Black Hole Parameters -----
G = 1          # Gravitational constant (scaled)
M = 50         # Mass of black hole (bada rakhenge = strong gravity)
dt = 0.05      # Time step

# ----- Create Stars Around Black Hole -----
num_stars = 200

# Random circular distribution
r = np.random.uniform(5, 15, num_stars)
theta = np.random.uniform(0, 2*np.pi, num_stars)

x = r * np.cos(theta)
y = r * np.sin(theta)

# Initial velocity (tangential so they orbit)
vx = -np.sin(theta) * np.sqrt(G*M/r)
vy = np.cos(theta) * np.sqrt(G*M/r)

# ----- Plot Setup -----
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor("black")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_title("Black Hole Gravity Simulation", color="white")

stars, = ax.plot([], [], 'wo', markersize=2)
blackhole, = ax.plot(0, 0, 'ro', markersize=8)

# ----- Update Function -----
def update(frame):
    global x, y, vx, vy

    # Distance from black hole
    r = np.sqrt(x**2 + y**2)

    # Avoid division by zero
    r[r < 0.5] = 0.5

    # Gravitational acceleration
    ax_g = -G * M * x / r**3
    ay_g = -G * M * y / r**3

    # Update velocity
    vx += ax_g * dt
    vy += ay_g * dt

    # Update position
    x += vx * dt
    y += vy * dt

    stars.set_data(x, y)
    return stars,

# ----- Run Animation -----
ani = FuncAnimation(fig, update, frames=400, interval=30)

# ----- Save Final Image for GitHub -----
plt.savefig("blackhole_snapshot.png", dpi=300)

plt.show()
