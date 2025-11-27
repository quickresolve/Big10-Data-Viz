# Big10-Data-Viz: Fight Song Data Visualizations Repository

This repository hosts two advanced data visualizations analyzing the creation history and lyrical content of college fight songs from Power Five conferences. The project utilizes Python to transform raw data into specialized graph representations that reveal hidden patterns in the songs' origins and shared language.


1. Sankey Diagram: Song Origin Path

[Song Origin Path: Student Writer -> Contest -> Official Status](/sankey_diagram.html)

## Project Description & Story

This visualization maps the journey a fight song takes from its inception to official status. The flow represents three sequential decision points, which are the main stages of a song's creation history: Was the author a Student Writer? > Was the song chosen via a Contest? > Is the song the Official Song?

The diagram tells a story about the standardization of fight songs, showing that most songs—regardless of whether they were written by a student—gain official status by bypassing a formal contest. The width of the flow ribbons makes these dominant paths immediately apparent.


### Technical Details
- Language: Python 
- Libraries: Pandas (for data aggregation), Plotly (for interactive rendering)
- Output File: [sankey_diagram_final.html](/sankey_diagram.html)

### How to Read the Diagram
- Nodes (Boxes): The vertical columns representing the three stages ('Student Writer', 'Contest Chosen', 'Official Song').

- Ribbons (Flows): The connections between the nodes. The thickness of a ribbon is directly proportional to the total number of songs that followed that exact path.

____________________________________________________________________________________

2. Chord Diagram: Trope Co-occurrence

   [Lyrical Trope Co-occurrence in Fight Songs (Chord Diagram)](/trope_co_occurrence_chord_diagram_final_labels.html)

## Project Description & Story
This visualization explores the lyrical DNA of college fight songs by examining the co-occurrence of nine common lyrical tropes (e.g., 'fight', 'victory', 'colors', 'rah', 'nonsense'). The visualization is built on a co-occurrence matrix that tallies how many songs feature any given pair of tropes simultaneously.

The story reveals which terms are most strongly associated with one another. For example, the thick ribbons connecting 'fight' and 'victory/win' show a strong lyrical association, while the thinner links associated with terms like 'nonsense' or 'spelling' indicate they are more isolated thematically. The diagram is excellent for comparing the relative frequency of co-occurrence.

### Technical Details
- Language: Python
- Libraries: Pandas (for matrix calculation), HoloViews (for graph visualization), Bokeh (rendering backend)
- Output File: [trope_co_occurrence_chord_diagram_final_labels.html](/trope_co_occurrence_chord_diagram_final_labels.html)

### How to Read the Diagram
- Nodes (Segments): The colored segments around the circle, each representing one of the nine lyrical tropes.

- Ribbons (Links): The connections inside the circle. The thickness of a ribbon indicates the count of songs in which both connected tropes appear.

- Color Tracing: Ribbons inherit the color of their source node, making it easy to trace all connections originating from a single trope.
