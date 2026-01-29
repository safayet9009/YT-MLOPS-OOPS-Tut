class chatbook:

    __user_id=1

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1

        self.username=''
        self.password=''
        self.loggedin=False

        self.__name='Default user' #(encapsulation)
        #self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod

    def set_id(val):
        chatbook.__user_id=val

#encapsulation and setter getter method
    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name=value

    def menu(self):
        user_input=input("""welcome to chatbook!! How would you like to process
                         1.press 1 to signup
                         2.press 2 to signin
                         3.press 3 to write a post
                         4.Press 4 to message a friend
                         5.Press any other key to exit' 
                         
                            """)
    
    


        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmasg()
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


    def my_post(self):
        if self.loggedin==True:
            txt=input('Enter your message here')

            print(f'following content has been posted-> {txt}')

        else:
            print('you need to signin first to post something..')
        print('\n')
        self.menu()

    def sendmasg(self):
        if self.loggedin==True:
            txt=input('enter your message here ->')

            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print('you need to signin first to message someone..')

        print('\n')

        self.menu()


#user1=chatbook()


    
