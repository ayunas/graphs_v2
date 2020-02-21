def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
​
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
​
        The key is the friend's ID and the value is the path.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue( [user_id] )
        # Create an empty dictionary to store visited users and social paths
        visited = {}
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = path[-1]
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                # Add it to the visited dictionary, with the path as the value
                visited[v] = path
                # Then add all FRIENDS to the back of the queue
                for friend_id in self.get_friends(v):
                    # COPY THE PATH
                    path_copy = path.copy()
                    # ADD FRIEND TO THE PATH
                    path_copy.append(friend_id)
                    q.enqueue(path_copy)
        return visited