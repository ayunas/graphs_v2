#store all values in the graph in an adjacency list
#perform a dfs on every ancestor of the starting node.  return the ancestor that has the longest dfs path
#if there are no ancestors for the starting_node, return -1
import sys
sys.path.append('../graph')
from graph import Graph


def earliest_ancestor(ancestors, start):
    # parents = {p for p,c in ancestors}
    # children = {c for p,c in ancestors}
    graph = Graph()
    for pc in ancestors: #pc = (parent,child)
        p,c = pc
        graph.add_edge(c,p)
    
    parents = {p for p,c in ancestors}

    paths = []
    for p in parents:
        dfs_path = graph.dfs(start,p)
        paths.append(dfs_path)
    
    valid_paths = [p for p in paths if p is not None and len(p) > 1]
    longest_path = max(valid_paths, key=len)
    
    print(longest_path)

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(ancestors,1)
