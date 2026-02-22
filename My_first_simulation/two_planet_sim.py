import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  # gravitational constant

# Star (fixed at center)
mass_star = 1.989e30
pos_star = np.array([0.0, 0.0])

# Planet 1
mass_p1 = 5.972e24
pos_p1 = np.array([1.5e11, 0.0])
vel_p1 = np.array([0.0, 30000.0])

# Planet 2 (farther + slower)
mass_p2 = 6.39e23
pos_p2 = np.array([2.2e11, 0.0])
vel_p2 = np.array([0.0, 24000.0])

dt = 60 * 60   # 1 hour timestep
steps = 5000

traj_p1 = []
traj_p2 = []

def gravity(pos, mass):
    r = pos_star - pos
    dist = np.linalg.norm(r)
    force_dir = r / dist
    force_mag = G * mass_star * mass / dist**2
    return (force_mag / mass) * force_dir

for _ in range(steps):

    # accelerations due to star
    acc_p1 = gravity(pos_p1, mass_p1)
    acc_p2 = gravity(pos_p2, mass_p2)

    # update velocities
    vel_p1 += acc_p1 * dt
    vel_p2 += acc_p2 * dt

    # update positions
    pos_p1 += vel_p1 * dt
    pos_p2 += vel_p2 * dt

    traj_p1.append(pos_p1.copy())
    traj_p2.append(pos_p2.copy())

traj_p1 = np.array(traj_p1)
traj_p2 = np.array(traj_p2)

# Plot both orbits
plt.plot(traj_p1[:,0], traj_p1[:,1], label="Planet 1")
plt.plot(traj_p2[:,0], traj_p2[:,1], label="Planet 2")
plt.scatter(0, 0, color="orange", label="Star")

plt.title("Two-Planet Orbital Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.axis("equal")

plt.savefig("two_planet_result.png", dpi=300)
plt.show()
