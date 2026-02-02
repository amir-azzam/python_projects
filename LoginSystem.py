class LoginSystem:
    def __init__(self):
        # Your code here
        self.users = {}
        self.logged_users = set()
    def register(self, username, password):
        if username in self.users and password in self.users:
            print("user already exists")
        else:
            self.users[username] = password
            self.users[password] = username
            print("user registered successfully")
    def login(self, username, password):
            if username in self.users:
                if self.users[username] == password:
                    self.logged_users.add(username)
                    print("user logged in successfully")
                else:
                    print("password doesn't match")
            else:
                print("user isn't in the system")
    def sign_out(self, username):
        if username in self.users:
            if username in self.logged_users:
                self.logged_users.remove(username)
                print("user signed out successfully")
            else:
                print("user is not logged in")
        else:
            print("user is not in the system")


        #solution 1 but error in test case 2

        # if username in self.users:
        #     if username in self.logged_users:
        #         print("user signed out successfully")
        #     else:
        #         print("user is not logged in")
        # else:
        #     print("user is not in the system")

        #solution 2 but same error

        # if username in self.users and username in self.logged_users:
        #     print("user signed out successfully")
        # elif username in self.users and username not in self.logged_users:
        #     print("user is not logged in")
        # elif username not in self.users:
        #     print("user is not in the system")