import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px

# Step 1: Load Data
# Using a common encoding (latin-1) to avoid the Unicode errors encountered previously.
# NOTE: If this fails, the user must insert the correct 'sep' and 'encoding' they used before.
try:
    df = pd.read_csv("fight-songs-updated.csv", encoding='latin-1')
except Exception:
    # Fallback if latin-1 still causes issues.
    df = pd.read_csv("fight-songs-updated.csv")

# Inspect the conference column unique values to find the exact name
print("Unique Conference Names:", df['conference'].unique())

# Step 2: Filter for Big Ten Conference
big_ten_df = df[df['conference'] == 'Big Ten'].copy()

# Step 3: Select Musical Fingerprint Metrics
fingerprint_metrics = [
    'song_name',
    'bpm',
    'sec_duration',
    'number_fights',
    'trope_count'
]
fingerprint_df = big_ten_df[fingerprint_metrics]

# Step 4: Check data types and presence of NaNs
print("\n--- Fingerprint Data Info ---")
fingerprint_df.info()

print("\n--- Fingerprint Data Head ---")
print(fingerprint_df.head().to_markdown(index=False))

# Check for non-numeric or missing data in metric columns
print("\n--- Missing Data Check ---")
print(fingerprint_df.isnull().sum())


# --- Data Preparation from previous step ---
# Re-filter data to ensure continuity, as the VM state can be reset.
# Assuming df is the full loaded DataFrame.
try:
    df = pd.read_csv("fight-songs-updated.csv", encoding='latin-1')
except Exception:
    df = pd.read_csv("fight-songs-updated.csv")
    
big_ten_df = df[df['conference'] == 'Big Ten'].copy()

fingerprint_metrics = [
    'song_name',
    'bpm',
    'sec_duration',
    'number_fights',
    'trope_count'
]
fingerprint_df = big_ten_df[fingerprint_metrics]

# --- Step 5: Normalize and Reshape Data ---

# Separate song name from numeric metrics
metric_cols = ['bpm', 'sec_duration', 'number_fights', 'trope_count']
data_to_scale = fingerprint_df[metric_cols]

# Initialize and fit the Min-Max Scaler (scales data to 0-1)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data_to_scale)

# Create a new DataFrame for the scaled values, retaining original song index
scaled_df = pd.DataFrame(scaled_data, columns=metric_cols, index=fingerprint_df.index)
scaled_df['song_name'] = fingerprint_df['song_name']

# Reshape the data from wide to long format
# This creates a row for every combination of (song, metric, scaled_value)
long_df = scaled_df.melt(
    id_vars='song_name',
    var_name='Metric',
    value_name='Scaled Value'
)

# Inspect the reshaped data
print("\n--- Scaled and Reshaped Data Head (Long Format) ---")
print(long_df.head().to_markdown(index=False))

# Save the transformed data for the user
long_df.to_csv('big_ten_musical_fingerprint_data.csv', index=False)



# Reload the long_df (since VM execution is separate)
long_df = pd.read_csv('big_ten_musical_fingerprint_data.csv')

# --- Step 6: Generate the Interactive Radar Chart (Plotly) ---

# Generate the Radar Chart
fig = px.line_polar(
    long_df,
    r='Scaled Value',
    theta='Metric',
    color='song_name',
    line_close=True, # Connects the last data point back to the first
    title="Big Ten Fight Songs: Musical Fingerprint (Min-Max Scaled)",
    hover_data={'Scaled Value': ':.2f'} # Display scaled value to 2 decimal places in hover
)

# Customize the chart appearance
fig.update_traces(fill='toself', opacity=0.3)
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1] # Ensure the radial axis ranges from 0 to 1 (the scaled range)
        )
    ),
    showlegend=False, # Hides the legend because there are too many songs (18)
)

# Save the interactive HTML file
fig.write_html("big_ten_musical_fingerprint_radar_chart.html")

