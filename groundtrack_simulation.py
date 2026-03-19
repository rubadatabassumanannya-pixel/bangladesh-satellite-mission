# groundtrack_simulation.py
import numpy as np
import matplotlib.pyplot as plt

# Earth constants
earth_radius = 6371        # km
altitude = 550             # km
mu = 398600                # km^3/s^2

# Satellite orbital radius
r = earth_radius + altitude

# Orbital velocity
v = np.sqrt(mu / r)

# Orbital period
T = 2 * np.pi * np.sqrt(r**3 / mu)  # in seconds

# Number of steps for simulation
steps = 1000

# Time array for one orbit
time = np.linspace(0, T, steps)

# Simple circular orbit in equatorial plane
theta = 2 * np.pi * time / T  # angle

x = r * np.cos(theta)
y = r * np.sin(theta)

# Convert orbit to latitude-longitude for ground track (simplified)
# Inclination for sun-synchronous orbit
inc = np.radians(97.6)  # SSO typical inclination
lat = np.degrees(np.arcsin(np.sin(inc) * np.sin(theta)))
lon = np.degrees(theta) % 360 - 180  # from -180 to +180

# Bangladesh location
bd_lat = 23.685
bd_lon = 90.356

# Check satellite passes near Bangladesh (±2 degrees)
passes = []
for la, lo, t in zip(lat, lon, time):
    if abs(la - bd_lat) <= 2 and abs(lo - bd_lon) <= 2:
        passes.append(t/60)  # time in minutes

# Plot ground track
plt.figure(figsize=(12,6))
plt.plot(lon, lat, label="Satellite Ground Track")
plt.scatter(bd_lon, bd_lat, color="red", label="Bangladesh Center")
plt.xlabel("Longitude (°)")
plt.ylabel("Latitude (°)")
plt.title("Satellite Ground Track Simulation")
plt.legend()
plt.grid(True)
plt.show()

# Print pass times
print("Satellite passes over Bangladesh at approximate minutes:")
print([round(p,1) for p in passes])
