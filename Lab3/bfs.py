#Author: Owolabi
#Date: 11/17/2025
#Purpose: Implements Breadth-First Search to compute the shortest path between two Vertex objects.
# bfs.py
from collections import deque

# STANDARD BFS (returns a path as a list of Vertex objects)
def bfs(start, goal):
    backpointer = {start: None}
    q = deque([start])

    while len(q) > 0:
        current = q.popleft()

        if current == goal:
            return construct_path(backpointer, goal)

        for nbr in current.adjacent:
            if nbr not in backpointer:
                backpointer[nbr] = current
                q.append(nbr)

    return None


def construct_path(backpointer, end):
    path = []
    v = end
    while v is not None:
        path.append(v)
        v = backpointer[v]
    path.reverse()
    return path


# ANIMATED BFS
# Yields: (current vertex, frontier list, visited list)
# map_plot will consume frames one at a time
def bfs_animated(start, goal):
    backpointer = {start: None}
    q = deque([start])
    visited = set([start])

    while len(q) > 0:
        current = q.popleft()

        # yield (current frame)
        yield current, list(q), list(visited)

        if current == goal:
            yield ("FOUND", construct_path(backpointer, goal))
            return

        for nbr in current.adjacent:
            if nbr not in visited:
                visited.add(nbr)
                backpointer[nbr] = current
                q.append(nbr)

    yield ("NO_PATH", None)


# BIDIRECTIONAL BFS (Breadcrumb Search)
def breadcrumb_bfs(start, goal):
    if start == goal:
        return [start]

    frontier_forward = deque([start])
    frontier_backward = deque([goal])

    back_f = {start: None}     # forward search backpointers
    back_b = {goal: None}      # backward search backpointers

    visited_f = {start}
    visited_b = {goal}

    while len(frontier_forward) > 0 and len(frontier_backward) > 0:

        # expand forward
        current = frontier_forward.popleft()

        for nbr in current.adjacent:
            if nbr not in visited_f:
                visited_f.add(nbr)
                back_f[nbr] = current
                frontier_forward.append(nbr)

                if nbr in visited_b:   # meet in middle
                    return merge_paths(back_f, back_b, nbr)

        # expand backward
        current = frontier_backward.popleft()

        for nbr in current.adjacent:
            if nbr not in visited_b:
                visited_b.add(nbr)
                back_b[nbr] = current
                frontier_backward.append(nbr)

                if nbr in visited_f:   # meet in middle
                    return merge_paths(back_f, back_b, nbr)

    return None


def merge_paths(back_f, back_b, meet):
    # Build forward part
    path1 = []
    v = meet
    while v is not None:
        path1.append(v)
        v = back_f[v]
    path1.reverse()

    # Build backward part
    path2 = []
    v = back_b[meet]
    while v is not None:
        path2.append(v)
        v = back_b[v]

    return path1 + path2
