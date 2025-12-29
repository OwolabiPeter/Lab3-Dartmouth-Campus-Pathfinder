#Author: Owolabi
#Date: 11/17/2025
#Purpose: Holds the vertex data structure + drawing functions

from cs1lib import draw_circle, set_stroke_width, draw_line
from cs1lib import set_fill_color, set_stroke_color, draw_text

VERTEX_RADIUS = 7
EDGE_WIDTH = 2
TEXT_OFFSET_X = 10
TEXT_OFFSET_Y = -10

class Vertex:
    def __init__(self, name, x, y):
        # name of the vertex (string)
        self.name = name
        # pixel coordinates on the map
        self.x = int(x)
        self.y = int(y)
        # list of adjacent Vertex objects
        self.adjacent = []

    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    def draw_vertex_with_name(self, r, g, b):
        # draw vertex
        self.draw_vertex(r, g, b)
        # label text
        set_stroke_color(1, 1, 1)
        draw_text(self.name, self.x + TEXT_OFFSET_X, self.y + TEXT_OFFSET_Y)

    def draw_edge(self, other, r, g, b):
        set_stroke_width(EDGE_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, other.x, other.y)

    def draw_all_edges(self, r, g, b):
        for v in self.adjacent:
            self.draw_edge(v, r, g, b)

    def is_on_vertex(self, mx, my):
        # Square hit-box
        return abs(mx - self.x) <= VERTEX_RADIUS and abs(my - self.y) <= VERTEX_RADIUS

    def __str__(self):
        s = self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: "
        for i in range(len(self.adjacent)):
            s += self.adjacent[i].name
            if i < len(self.adjacent) - 1:
                s += ", "
        return s
