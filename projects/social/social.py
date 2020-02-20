class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, friends):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        sg.populate_graph(10, 2)  # Creates 10 users with an average of 2 friends each
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        import random
        import names
        #for loop u times.  u is # of users.  user can be rep'ed by an integer
            #add user_id to the graph
            #generate a friends set of random length of randint(1,2*friends-1).

        # Add users
        for u in range(num_users):
            username = names.get_first_name()
            self.add_user(username)

        # Create friendships
        for u in self.users:
            friend_count = random.randint(0,2*friends)
            # friend_count = random.randint(1,3)
            # print('fc',friend_count, end=' ')
            for i in range(friend_count):
                network = [user for user in self.users if user != u]
                friend_id = random.choice(network)
                self.friendships[u].add(self.users[friend_id])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('users: ', sg.users,'\n')
    print('friendship per user_id', sg.friendships)
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
