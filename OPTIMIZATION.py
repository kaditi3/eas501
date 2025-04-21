temps_fahrenheit = [32, 68, 77, 104]
temps_celsius = []

for temp in temps_fahrenheit:
    celsius = (temp - 32) * (5 / 9)
    temps_celsius.append(celsius)
print(temps_celsius)

# Functional approach using map
temps_fahrenheit = [32, 68, 77, 104]
temps_celsius = list(map(lambda f: (f - 32) * (5 / 9), temps_fahrenheit))
print(temps_celsius)

import numpy as np

# Initialize population data with NumPy arrays
time_steps = 500
lynx_population = np.zeros(time_steps + 1)
hare_population = np.zeros(time_steps + 1)
lynx_population[0] = hare_population[0] = 1.1

# Vectorized simulation
lynx_change = np.zeros(time_steps)
hare_change = np.zeros(time_steps)

# Calculate changes with vectorized operations
lynx_change = 0.01 - 0.01 * hare_population[:-1]
hare_change = 0.01 * lynx_population[:-1] - 0.01

# Apply cumulative product to simulate population changes
lynx_population[1:] = lynx_population[0] * np.cumprod(1 + lynx_change)
hare_population[1:] = hare_population[0] * np.cumprod(1 + hare_change)

import numpy as np
daily_AQI =  [45, 50, 78, 85, 34, 90, 72, 88, 95, 89, 76]
is_safe= list(map(daily_AQIifelse AQI>80)
