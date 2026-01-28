class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""welcome to chatbook!! How would you like to process\n'
                         1.press 1 to signup
                         2.press 2 to signin
                         3.press 3 to write a post
                         4.Press 4 to message a friend
                         5.Press any other key to exit' """)
    

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()


    def signup(self):
        email=input("Enter your email: ")
        pwd=input ("Enter your password: ")
        self.username=email
        self.password=pwd
        print("Signup successful!")
        print('\n')
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by pressing 1")
        else:
            uname=input("Enter your username/email: ")
            pwd=input("Enter your password: ")
            if self.username==uname and self.password==pwd:
                print("Signin successful!")
                self.loggedin=True
            else:
                print("please input correct credentials..")

            print('\n')

            self.menu()




user1=chatbook()


    
