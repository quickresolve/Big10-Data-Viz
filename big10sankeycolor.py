import plotly.graph_objects as go

# --- Data Preparation ---
node_labels = ['Student Writer: Yes', 'Student Writer: No', 'Student Writer: Unknown', 'Contest Chosen: Yes', 'Contest Chosen: No', 'Official Song: Yes', 'Official Song: No']
link_source = [1, 4, 1, 4, 1, 3, 2, 4, 0, 4, 0, 4, 0, 3, 0, 3]
link_target = [4, 6, 4, 5, 3, 5, 4, 5, 4, 6, 4, 5, 3, 6, 3, 5]
link_value = [3, 3, 23, 23, 4, 4, 3, 3, 3, 3, 23, 23, 1, 1, 5, 5]
link_color = ['rgba(255, 99, 132, 0.8)', 'rgba(255, 99, 132, 0.8)', 'rgba(54, 162, 235, 0.8)', 'rgba(54, 162, 235, 0.8)', 'rgba(255, 206, 86, 0.8)', 'rgba(255, 206, 86, 0.8)', 'rgba(75, 192, 192, 0.8)', 'rgba(75, 192, 192, 0.8)', 'rgba(153, 102, 255, 0.8)', 'rgba(153, 102, 255, 0.8)', 'rgba(255, 159, 64, 0.8)', 'rgba(255, 159, 64, 0.8)', 'rgba(199, 199, 199, 0.8)', 'rgba(199, 199, 199, 0.8)', 'rgba(140, 80, 20, 0.8)', 'rgba(140, 80, 20, 0.8)']

# --- Create the Sankey Diagram ---
fig = go.Figure(data=[go.Sankey(
    # Configuration for the nodes (the boxes)
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=node_labels,
        color="#7f7f7f"
    ),
    # Configuration for the links (the flow ribbons)
    link=dict(
        source=link_source,
        target=link_target,
        value=link_value,
        # Unique color for each path
        color=link_color 
    )
)])

fig.update_layout(
    title_text="Song Origin Path: Student Writer → Contest → Official Status (Distinguished by Unique Path Color)",
    font_size=10
)

# Use fig.write_html('sankey_diagram_unique_paths.html') to save locally
fig.show()