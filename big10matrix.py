import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv(
    "fight-songs-updated.csv"
)

# 1. Identify the binary trope columns
trope_cols = ['fight', 'victory', 'win_won', 'rah', 'nonsense', 'colors', 'men', 'opponents', 'spelling']

# 2. Convert 'Yes'/'No' (and 'Unknown'/'No' if they exist, but mostly 'Yes'/'No') to 1/0 for matrix calculation
# The logic handles 'Unknown' by treating it as 'No' (0) if it appears in these columns, 
# although based on info() only 'year' and 'student_writer' had 'Unknown', not these binary trope columns.
binary_df = df[trope_cols].apply(lambda x: x.map({'Yes': 1, 'No': 0, 'Unknown': 0}))

# 3. Calculate the Co-occurrence Matrix (M^T * M)
# M is the matrix of binary trope indicators. M^T * M gives the count of shared 'Yes' occurrences.
co_occurrence_matrix = binary_df.T.dot(binary_df)

# 4. Save the matrix to CSV for the user
co_occurrence_matrix.to_csv('trope_co_occurrence_matrix.csv')

print("Generated trope_co_occurrence_matrix.csv")

# Display the matrix head for immediate review
print("\nCo-occurrence Matrix Head (Counts of shared 'Yes' values):\n")
print(co_occurrence_matrix.head().to_markdown())

# Display descriptive statistics of the matrix
print("\nMatrix Info:")
print(co_occurrence_matrix.info())