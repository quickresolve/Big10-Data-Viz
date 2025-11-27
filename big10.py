import plotly.graph_objects as go

# --- Data Preparation ---
node_labels = [
    'Student Writer: Yes', 'Student Writer: No', 'Student Writer: Unknown',
    'Contest Chosen: Yes', 'Contest Chosen: No',
    'Official Song: Yes', 'Official Song: No'
]

# The lists 
link_source = [1, 4, 1, 4, 1, 3, 2, 4, 0, 4, 0, 4, 0, 3, 0, 3]
link_target = [4, 6, 4, 5, 3, 5, 4, 5, 4, 6, 4, 5, 3, 6, 3, 5]
link_value = [3, 3, 23, 23, 4, 4, 3, 3, 3, 3, 23, 23, 1, 1, 5, 5]

# --- Create the Sankey Diagram ---
try:
    fig = go.Figure(data=[go.Sankey(
        # Configuration for the nodes (the boxes)
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=node_labels,
            # Optional: Add color for each node based on the category
        ),
        # Configuration for the links (the flow ribbons)
        link=dict(
            source=link_source,
            target=link_target,
            value=link_value
        )
    )])

    fig.update_layout(
        title_text="Song Origin Path: Student Writer → Contest → Official Status",
        font_size=10
    )

    # Save to HTML
    fig.write_html('sankey_diagram.html')
    print("Successfully generated 'sankey_diagram.html'")

except ImportError:
    print("Plotly is not installed in this environment.")
except Exception as e:
    print(f"An error occurred: {e}")