class Users:
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password


if __name__ == '__main__':
    user1 = Users ('user1','password1')
    user2 = Users ('user2','password2')
    user3 = Users ('user3','password3')

    utenti = [user1,user2,user3]


