def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
​
        This should be done using recursion.
        """
        # Check if the node is visited
        if visited is None:
            visited = set()
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            # Print
            print(starting_vertex)
            # Call DFT_Recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """
        # initialize visited if it's not yet initialized
        if visited is None:
            visited = set()
        # initialize path if it's not yet initialized
        if path is None:
            path = []
        # Check if starting vertex has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited, add it to the path
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # If starting_vertex is destination:
            if starting_vertex == destination_vertex:
                return path_copy
            # Call DFS recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path