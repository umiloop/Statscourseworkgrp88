import random
# The `random` module generates random x and y coordinates for simulating dart throws, which is vital for estimating pi using Monte Carlo simulation.
# Function to simulate a dart throw.
def montecarlo_pifinding(n):
    hits = 0
    misses = 0
    for i in range(n):
        # Generating random x and y coordinates on the Cartesian plane.
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        # Checking whether the dart lands within the circular area.
        if distance <= 1:
            hits += 1
        else:
            misses += 1
    
    # Calculating the probability of hitting inside the circle and the probability of a miss as percentages.
    probability_hit = (hits / n) * 100
    probability_miss = (misses / n) * 100
    
    # Estimating the value of pi based on the theoretical approach.
    estimated_pivalue = 4 * (hits / n)
    return estimated_pivalue, hits, misses, probability_hit, probability_miss

# Obtaining user input for the total number of darts thrown in the simulation.
n = int(input("Enter the number of darts for the simulation > "))

# Invoking the function to perform the simulation.
pi, hits, misses, probability_hit, probability_miss = montecarlo_pifinding(n)
print("\nDartboard Simulation Results:\n")
print(f"Number of Dart hits:  {hits}/{n}")
print(f"Number of Dart misses:  {misses}/{n}")
print(f"Probability of a hit: {probability_hit:.2f}%")
print(f"Probability of a miss: {probability_miss:.2f}%")
print(f"Estimated value of pi using {n} darts : {pi}")



