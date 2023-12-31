import random  #Importing the random module for generating dice rolls

#Set the number of dice to roll
num_dice = 10

#Get user input for the number of simulations
num_simulations = int(input("Enter the number of simulations: "))

def estimate_dice_probability(num_dice_to_roll, num_simulations):
    #Simulates dice rolls to estimate the probability of a specific sum

    successful_rolls = 0  #Counter for successful outcomes (sum of 32)

    for _ in range(num_simulations):
        #Generate a list of random dice rolls
        roll_results = [random.randint(1, 6) for _ in range(num_dice_to_roll)]

        #Check if the sum of the rolls matches the target sum
        if sum(roll_results) == 32:
            successful_rolls += 1

    #Calculate and return the estimated probability
    return successful_rolls / num_simulations

#Call the function to simulate and calculate the probability
estimated_probability = estimate_dice_probability(num_dice, num_simulations)

#Output the estimated probability
print("Simulated Probability:", estimated_probability)