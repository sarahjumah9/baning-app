class Client:
    def __init__(self, name, age, gender, membership_type):
        self.name = name
        self.age = age
        self.gender = gender
        self.membership_type = membership_type

    def user_details(self):
        print(" user details! ")
        print("Name:  " + self.name)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)
        print("Membership_type: " + self.membership_type)

class Bank(Client):
    def __init__(self, name,age,gender, membership_type):
        super().__init__(name,age, gender, membership_type)
        self.balance=0

    def balance(self, amount):
        self.amount = amount
        self.balance =self.balance+amount
        print("Your account balance is "+ self.balance)



u1 = Client("Sarah", 26, "female", "silver")
u1.user_details()