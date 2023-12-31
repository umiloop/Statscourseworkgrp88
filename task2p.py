from itertools import product

def count_ways_to_sum(target, dice_count, sides_count):
    total_count = 0
    for dice_roll in product(range(1, sides_count + 1), repeat=dice_count):
        if sum(dice_roll) == target:
            total_count += 1
    return total_count

if __name__ == "__main__":
    target = int(input("Enter the target sum: "))
    dice_count = int(input("Enter the number of dice: "))
    sides_count = int(input("Enter the number of sides on each die: "))
    
    total_outcomes = sides_count ** dice_count
    ways_to_reach_target = count_ways_to_sum(target, dice_count, sides_count)
    
    probability_exact = ways_to_reach_target / total_outcomes
    print("Probability (exact calculation):", probability_exact)
