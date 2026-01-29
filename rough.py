from mini_project import chatbook

user1=chatbook()
print(user1.id)

# getter and setter method

# print(user1.get_name())

# user1.set_name('Agent x')
# print(user1.get_name())


# Using static method directly from class rather than obj
chatbook.set_id(10)

user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)