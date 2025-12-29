#Author: Owolabi
#Date: 11/17/2025
#Purpose: Reads dartmouth_graph.txt and builds the vertex dictionary

from vertex import Vertex

def create_vertex_dictionary(filename):
    vertex_dict = {}
    lines = []

    # Read lines and create vertices
    with open(filename) as f:
        for line in f:
            line = line.strip()
            lines.append(line)

            name_part, neighbors_part, coords_part = line.split(";")

            name = name_part.strip()

            # parse coordinates
            x_str, y_str = coords_part.split(",")
            x = int(x_str.strip())
            y = int(y_str.strip())

            vertex_dict[name] = Vertex(name, x, y)

    # Now that all Vertex objects exist, fill adjacency lists
    for line in lines:
        name_part, neighbors_part, coords_part = line.split(";")
        name = name_part.strip()

        # neighbors are comma-separated
        neighbors = [n.strip() for n in neighbors_part.split(",")]

        for n in neighbors:
            if n != "":
                vertex_dict[name].adjacent.append(vertex_dict[n])

    return vertex_dict
