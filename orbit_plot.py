import numpy as np
import matplotlib.pyplot as plt

earth_radius = 6371
altitude = 550

r = earth_radius + altitude

theta = np.linspace(0, 2*np.pi, 500)

x = r * np.cos(theta)
y = r * np.sin(theta)

earth_x = earth_radius * np.cos(theta)
earth_y = earth_radius * np.sin(theta)

plt.figure()
plt.plot(x, y, label="Satellite Orbit")
plt.plot(earth_x, earth_y, label="Earth")

plt.axis("equal")
plt.xlabel("km")
plt.ylabel("km")
plt.legend()

plt.title("Satellite Orbit Simulation")

plt.show()
