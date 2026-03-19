import numpy as np

# Earth constants
earth_radius = 6371       # km
altitude = 550            # km
mu = 398600               # Earth's gravitational parameter

# Orbital radius
r = earth_radius + altitude

# Orbital velocity
v = np.sqrt(mu / r)

# Orbital period
T = 2 * np.pi * np.sqrt(r**3 / mu)

print("Orbital Radius:", r, "km")
print("Orbital Velocity:", round(v,2), "km/s")
print("Orbital Period:", round(T/60,2), "minutes")
