# Bangladesh Satellite Mission Simulation

Python simulation of a circular low Earth orbit (LEO) satellite, with orbital parameter calculation, orbit visualization and a ground-track analysis of passes over Bangladesh.

## Objective
- Compute key orbital parameters (velocity, period, orbits per day) for a 550 km circular orbit.
- Visualize the orbit and its ground track.
- Estimate when the satellite passes over Bangladesh, as a first step in Earth-observation mission planning.

## Model and assumptions
| Parameter | Value |
|---|---|
| Orbit type | Circular LEO, two-body (Keplerian) |
| Altitude | 550 km |
| Earth radius | 6371 km |
| Orbital radius (r) | 6921 km |
| Gravitational parameter (mu) | 398600 km^3/s^2 |
| Inclination | 97.6 deg (sun-synchronous value for this altitude) |
| Target | Bangladesh centre, 23.685 N, 90.356 E |

**Equations**

Orbital velocity: `v = sqrt(mu / r)`

Orbital period: `T = 2 * pi * sqrt(r^3 / mu)`

## Results

### Orbital parameters
| Parameter | Value |
|---|---|
| Orbital velocity | 7.59 km/s |
| Orbital period | 95.5 min |
| Orbits per day | about 15 |

### Ground-track analysis
A "pass" is counted when the sub-satellite point falls within +/-2 deg latitude and longitude of the Bangladesh centre point.

| Pass | Time after start (min) | Latitude | Longitude |
|---|---|---|---|
| [fill from your script output] | | | |

> Paste the pass times your script produces. State the start epoch and the simulation duration used.

### Visualizations
![Orbit visualization]<img width="640" height="480" alt="orbitpath" src="https://github.com/user-attachments/assets/8c6817d3-150e-45db-aeb7-61090ce741b5" />

![Ground track over Bangladesh]<img width="1000" height="500" alt="groundtrack" src="https://github.com/user-attachments/assets/57b3f476-5b3e-4423-917f-35f57fc2e2d5" />

## Limitations
- **Two-body model only.** No J2 oblateness, atmospheric drag or other perturbations. A real sun-synchronous orbit depends on J2 precession, so the 97.6 deg inclination is used here as a given value, not derived by the model.
- **Pass detection is crude.** A +/-2 deg box around one point is not a sensor footprint. It ignores swath width, elevation angle and ground-station visibility.
- **Single day, single satellite.** No revisit statistics yet.
- [Confirm and state whether Earth rotation is included in the ground track. It must be, or the track will repeat over the same longitude every orbit.]

## Run it
```bash
pip install numpy matplotlib
pip install cartopy   # optional, for map plots
python [your_script_name].py
```

## Next steps
1. Replace the box test with a footprint test based on sensor field of view and Earth curvature.
2. Simulate multiple days and report revisit time statistics.
3. Add J2 perturbation and compare the ground track drift.
4. Add payload constraints (swath width, resolution) and compare candidate altitudes.

## Tools
Python, NumPy, Matplotlib, Cartopy (optional).
