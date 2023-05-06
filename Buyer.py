from User import User
from Product import Product

class Buyer(User):

    def __init__(self:str, name:str, password:str, email:str,address:str,phone_number:int)->None:
        super().__init__(name, password, email)
        self.__address=address
        self.__phone_number=phone_number

    def buy_products(self) -> None:
        #
        return

    def make_payment(self) -> None:
        # here we will make a function to access bank acount and make a payment
        return

    def add_to_cart(self, product: Product) -> None:
        self.cart.append(product)

    def delete_from_cart(self, product: Product) -> None:
        if product in self.cart:
            self.cart.remove(product)

    def select_amount(self, product: Product, amount: int) -> None:
        # here we will select amount of product
        return

    def add_to_favorites(self, product: Product) -> None:
        self.favorites.append(product)