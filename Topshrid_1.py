class User:
    def __init__(self, name, age, password):
        self.name = name
        self._age = age
        self.__password = password

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Yosh 0 dan kichik bo'lishi mumkin emas!")
        else:
            self._age = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 6:
            print("Parol kamida 6 ta belgi bo'lishi kerak!")
        else:
            self.__password = value

    def __str__(self):
        return f"Foydalanuvchi: {self.name}, Yosh: {self.age}"

    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, password='{self.__password}')"


user1 = User("Ali", 20, "ali123")
user2 = User("Vali", 18, "vali456")

print(user1)
print(user2)

print("Ali yoshi:", user1.age)

user1.age = 21
print("Yangi yosh:", user1.age)

user1.age = -5

user1.password = "new123"
print("Yangi parol:", user1.password)

user2.password = "123"

print(repr(user1))
print(repr(user2))