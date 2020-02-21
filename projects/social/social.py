# import sys
# sys.path.append('../graph')
# from util import Queue

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size > 0:
            return self.queue.pop(0)
        else:
            return None
    @property
    def size(self):
        return len(self.queue)
    def __repr__(self):
        return str(self.queue)


class User:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
    
    def bfs(self,start_id,end_id):
        q = Queue()
        q.enqueue([start_id])
        visited = set()

        while q.size > 0:
            path = q.dequeue()
            print(path)
            friend_id = path[-1]

            if friend_id not in visited:
                if friend_id == end_id:
                    return path
                visited.add(friend_id)

            f_friends = self.get_friends(friend_id)

            for f in f_friends:
                new_path = path.copy()
                new_path.append(f.id)
                q.enqueue(new_path)
            


    
    def get_friends(self,user_id):
        friends = []
        for f in self.friendships[user_id]:
            friends.append(f)
        return friends

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
        self.users[self.last_id] = User(name,self.last_id)
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
            friend_count = random.randint(1,2*friends-1)
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
        {Joe : [Jeff,May], Frank : [Ben,Simon,Jacob]}
        for each friend of user_id, do a BFT.
        add each friend to the visited object.
        """
        q = Queue()
        q.enqueue([user_id])
        visited = {}
        print('getting extended friend network for: ', self.users[user_id].name)
        while q.size > 0:
            path = q.dequeue()
            f_id = path[-1]

            if f_id not in visited:
                visited[f_id] = path

                for ff in self.get_friends(f_id):
                    new_path = path.copy()
                    new_path.append(ff.id)
                    q.enqueue(new_path)
        
        for user_id in visited:
            user_name = self.users[user_id].name
        
        ext_net = {self.users[u_id].name : visited[u_id] for u_id in visited}
        
        for user in ext_net:
            f_path = [self.users[f_id].name for f_id in ext_net[user]]
            # f_path.reverse()
            ext_net[user] = f_path

        for user in ext_net:
            if len(ext_net[user]) == 1 and user == ext_net[user][-1]:
                del ext_net[user]
                break
        
        return ext_net  #extended network
        # return visits

        # friends = self.get_friends(user_id)
        # print('friends', friends)
        # for f in friends:
        #     f_friends = self.get_friends(f.id)
        #     print('F_FRIENDS', f_friends)
        #     for ff in f_friends:
        #         print('ff.id',ff.id)
        #         bfs = self.bfs(user_id,ff.id)
        #         print(bfs)
        #         visited[ff.id] = bfs
        # visited = {}  # Note that this is a dictionary, not a set
        # return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('users: ', sg.users,'\n')
    print('friendship per user_id', sg.friendships, '\n')
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    x = sg.get_all_social_paths(5)
    print(x)


