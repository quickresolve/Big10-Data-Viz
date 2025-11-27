import holoviews as hv
from holoviews import opts
import pandas as pd
hv.extension('bokeh')

# --- Define Node Colors ---
trope_colors = [
    '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00',
    '#ffff33', '#a65628', '#f781bf', '#999999'
]

# --- Load and Transform Co-occurrence Matrix (Assumed correct) ---
co_occurrence_matrix = pd.read_csv('trope_co_occurrence_matrix.csv', index_col=0)

edge_list_df = co_occurrence_matrix.stack().reset_index()
edge_list_df.columns = ['source', 'target', 'value']
edge_list_df = edge_list_df[edge_list_df['source'] != edge_list_df['target']]


# --- Generate Chord Diagram ---
chord = hv.Chord(edge_list_df, ['source', 'target'], 'value') 

# Apply styling options
chord.opts(
    opts.Chord(
        # FINAL FIX: Pass the string name 'source' directly. Bokeh should recognize this as a field name.
        node_color='source', 
        cmap=trope_colors,
        
        # Ribbons Coloring: Apply the same fix to the edge color.
        edge_color='source',
        edge_cmap=trope_colors,
        
        # Node and Label Settings
        label_text_font_size='10pt',
        padding=0.1,
        
        # General Plot Aesthetics
        width=800,
        height=800,
        title='Lyrical Trope Co-occurrence in Fight Songs (Chord Diagram)',
        tools=['hover']
    )
)

# --- Save to HTML ---
output_filename = 'trope_co_occurrence_chord_diagram_final_labels.html'
hv.save(chord, output_filename)

print(f"\nSuccessfully generated the Chord Diagram HTML file: {output_filename}")