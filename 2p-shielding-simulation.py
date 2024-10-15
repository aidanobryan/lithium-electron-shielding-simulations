import numpy as np

a_0 = 1 # Set the Bohr radius to 1 for simplicity (this will not affect the results).
total_Z = 0

def P(r):
    return 1/24 * 1/(a_0**5) * r**4 * np.exp(-r/a_0)

for i in range(10000):
    # Generate a random real number from 0 to 15:
    r = np.random.uniform(0, 15)
    # Generate a random real number from 0 to 1:
    y = np.random.uniform(0, 1)

    while y >= P(r):
        r = np.random.uniform(0, 15)
        y = np.random.uniform(0, 1)
    
    # This process obeys the probability distribution since each radii will have a probability to from 0 to 1 given by the function P(r) and y gives a random number in this same range.

    Z = 1

    if r < a_0:
        Z = 3
    
    total_Z += Z

Z_eff = total_Z / 10000

print("Z_eff =", Z_eff)