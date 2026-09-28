class Product:
    def __init__(self, name, category, price):
        self.name = name
        self._category = category
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Price 0 yoki undan kichik bo'lishi mumkin emas!")
        else:
            self.__price = value

    def __str__(self):
        return f"Mahsulot: {self.name}, Kategoriya: {self._category}, Narxi: {self.price} so'm"

    def __repr__(self):
        return f"Product('{self.name}', '{self._category}', {self.__price})"

product1 = Product("Olma", "Meva", 10000)
product2 = Product("Telefon", "Elektronika", 3000000)
product3 = Product("Kitob", "Ta'lim", 50000)

print(product1)
print(product2)
print(product3)

product1.name = "Qizil olma"
print(product1)

print("Telefon narxi:", product2.price)

product2.price = 3500000
print("Yangi telefon narxi:", product2.price)

product3.price = 0

print(repr(product1))
print(repr(product2))
print(repr(product3))