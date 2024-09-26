import pandas as pd
import random

# Load the file into a DataFrame
file_path = 'data_files/DISC_Sign_Up_Sheet.csv'  # Adjusted to use the correct file name
datafile = pd.read_csv(file_path)

# Print original data (for debugging purposes)
print("Original Data:")
print(datafile)

# Normalize the 'email' column (optional, to strip spaces and convert to lowercase)
datafile['email'] = datafile['email'].str.strip().str.lower()

# Check for duplicates based only on the 'email' column
duplicates = datafile[datafile.duplicated(subset=['email'], keep=False)]

# Display duplicates (for debugging purposes)
if not duplicates.empty:
    print("Duplicates found based on email:")
    print(duplicates)
else:
    print("No duplicates found based on email.")

# Remove duplicates and keep only the first occurrence (based on 'email')
datafile_cleaned = datafile.drop_duplicates(subset=['email'], keep='first')

# Print cleaned data (for debugging purposes)
print("Cleaned Data (Duplicates Removed):")
print(datafile_cleaned)

# Save the cleaned file to a new CSV
cleaned_file_path = 'data_files/cleaned_file.csv'
datafile_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned file saved to {cleaned_file_path}")

# Select a random row for a prize
if not datafile_cleaned.empty:
    random_winner = datafile_cleaned.sample(n=1)  # Select one random row
    print("The selected winner is:")
    print(random_winner)
    
    # Save the random winner to a new file
    winner_file_path = 'data_files/random_winner.csv'
    random_winner.to_csv(winner_file_path, index=False)
    print(f"Random winner saved to {winner_file_path}")
else:
    print("No data available to select a winner.")