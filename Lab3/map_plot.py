#Author: Owolabi
#Date: 11/17/2025
#Purpose: Displays the Dartmouth map and graph, allows the user to interact

from cs1lib import *
from load_graph import create_vertex_dictionary
from bfs import bfs, bfs_animated, breadcrumb_bfs

WIDTH = 1012
HEIGHT = 811

vertex_dict = create_vertex_dictionary("dartmouth_graph.txt")
map_img = load_image("dartmouth_map.png")

start_vertex = None
goal_vertex = None

mouse_x = 0
mouse_y = 0

# For animation
animation_generator = None
is_animating = False
use_breadcrumb = False


# Mouse handlers
def mouse_press(mx, my):
    global start_vertex, animation_generator, is_animating

    # clicking picks new start
    for v in vertex_dict.values():
        if v.is_on_vertex(mx, my):
            start_vertex = v
            is_animating = False
            animation_generator = None


def mouse_move(mx, my):
    global mouse_x, mouse_y
    mouse_x = mx
    mouse_y = my


# Keyboard handler
# a = toggle animation
# b = toggle breadcrumb search
def key_press(k):
    global is_animating, animation_generator, use_breadcrumb

    if k == "a":  # toggle animated BFS
        if start_vertex is not None and goal_vertex is not None:
            is_animating = True
            animation_generator = bfs_animated(start_vertex, goal_vertex)

    if k == "b":  # toggle breadcrumb search
        use_breadcrumb = not use_breadcrumb


# Draw loop
def draw():
    global goal_vertex, is_animating, animation_generator

    draw_image(map_img, 0, 0)

    # Identify goal vertex by hover
    goal_vertex = None
    if start_vertex is not None:
        for v in vertex_dict.values():
            if v.is_on_vertex(mouse_x, mouse_y):
                goal_vertex = v

    # Draw graph edges + vertices (blue)
    for v in vertex_dict.values():
        v.draw_all_edges(0, 0, 1)
    for v in vertex_dict.values():
        v.draw_vertex_with_name(0, 0, 1)

    #No BFS if missing start/goal
    if start_vertex is None or goal_vertex is None or start_vertex == goal_vertex:
        return

    # ANIMATED BFS MODE
    if is_animating and animation_generator is not None:
        frame = next(animation_generator, None)

        if frame is None:
            is_animating = False
            return

        if frame[0] == "FOUND":
            path = frame[1]
            draw_path(path)
            is_animating = False
            return

        current, frontier, visited = frame

        # visited: gray
        for v in visited:
            v.draw_vertex(0.6, 0.6, 0.6)

        # frontier: yellow
        for v in frontier:
            v.draw_vertex(1, 1, 0)

        # current: green
        current.draw_vertex(0, 1, 0)

        return

    # NORMAL BFS OR BREADCRUMB BFS
    if use_breadcrumb:
        path = breadcrumb_bfs(start_vertex, goal_vertex)
    else:
        path = bfs(start_vertex, goal_vertex)

    if path is not None:
        draw_path(path)


# helper: draw a path in red
def draw_path(path):
    for i in range(len(path) - 1):
        path[i].draw_edge(path[i+1], 1, 0, 0)
    for v in path:
        v.draw_vertex(1, 0, 0)


start_graphics(draw, width=WIDTH, height=HEIGHT,
               mouse_press=mouse_press, mouse_move=mouse_move,
               key_press=key_press)
