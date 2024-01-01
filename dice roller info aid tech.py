import random

def roll_dice(num_faces=6):
    return random.randint(1, num_faces)

# Example usage:
num_faces = 6  # Change this value to simulate different dice (e.g., 4-sided, 10-sided, etc.)
result = roll_dice(num_faces)
print(f"You rolled a {num_faces}-sided dice and got: {result}")
