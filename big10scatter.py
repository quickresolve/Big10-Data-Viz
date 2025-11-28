import pandas as pd
import numpy as np

file_path = 'fight-songs-updated.csv'
df = pd.read_csv(file_path)

# Check the data types for the 3D axes
print(df.info())

import plotly.express as px

# Define the axes and color
x_axis = 'bpm'
y_axis = 'number_fights'
z_axis = 'trope_count'
color_dim = 'conference'

# Generate the 3D Scatter Plot (Aggression-Pace-Complexity Signature)
fig = px.scatter_3d(df, 
                    x=x_axis, 
                    y=y_axis, 
                    z=z_axis,
                    color=color_dim,
                    hover_data=['school', 'song_name'],
                    title='3D Signature Space of College Fight Songs by Conference'
                   )

# Customize the axes titles for better readability
fig.update_layout(scene = dict(
                    xaxis_title=f'{x_axis} (Pace)',
                    yaxis_title=f'{y_axis} (Aggression)',
                    zaxis_title=f'{z_axis} (Lyrical Complexity)'))

# Save the plot to an HTML file
plot_filename = 'fight_song_3d_signature_space.html'
fig.write_html(plot_filename)