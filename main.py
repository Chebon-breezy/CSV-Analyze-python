import pandas as pd
import os

# Load the CSV file
df = pd.read_csv('states.csv')

# Calculate the average difficulty rating for each clue
clue_ratings = df.groupby('clue')['difficulty'].mean()

# Save the results to a new CSV file in the current working directory
output_path = os.path.join(os.getcwd(), 'clue_ratings.csv')
clue_ratings.to_csv(output_path, header=['average_difficulty'])

# Print the results
print(clue_ratings)
