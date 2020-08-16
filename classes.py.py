#!/usr/bin/env python
# coding: utf-8

# In[111]:


class Restraunt():
    def __init__(self, restraunt_name, cuisine_type):
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restraunt(self):
        print(f"You like {self.restraunt_name.title()} restraunt.")
        print(f"In this restraunt prevails {self.cuisine_type.title()}")
        print(f"Consumer ordered: {self.number_served}")
    def open_restraunt(self):
        print(f"The {self.restraunt_name.title()} opened.")
    def set_number_served(self, mileage):
        self.number_served = mileage
    def increment_number_served(self):
        self.number_served += 1
    def printed_consumer_ordered(self):
        print(f'{self.number_served}')
        
        
class IceCreamStand(Restraunt):
    def __init__(self, restraunt_name, cuisine_type):
        super().__init__(restraunt_name, cuisine_type)
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.flavors = ['apples','pineapples','chocolates','vinograds']
        
    def ice_cream_printed(self):
        print(f'{self.restraunt_name.upper()} have got this ice cream:')
        for flavor in self.flavors:
                 
            print(flavor.title())
        
restraunt1 = Restraunt('mcdonalds','usa')
restraunt1.describe_restraunt()
restraunt1.open_restraunt()
restraunt1.set_number_served(10)
restraunt1.describe_restraunt()
restraunt1.increment_number_served()
restraunt1.describe_restraunt()
restraunt1.increment_number_served()
restraunt1.printed_consumer_ordered()
restraunt2 = IceCreamStand('icebaby','usa')
restraunt2.describe_restraunt()
restraunt2.ice_cream_printed()


# In[ ]:





# In[110]:


class User():
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 1
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(full_name.title())
        print(f"User location: {self.location.title()}")
        print(f"Age users: {self.age}")
    def greet_user(self):
        print(f"Hello, Dear {self.first_name.title()} {self.last_name.title()}")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
class Privileges():
    def __init__(self, privileges = ['разрешено добавлять сообщения','разрешено удалять пользователей','разрешено банить']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())
    
        
class Admin(User):
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        self.privileges = Privileges()
        

user3 = Admin('harry','beran', 'moscow',44)
user3.describe_user()
user3.greet_user()
user3.privileges.show_privileges()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




