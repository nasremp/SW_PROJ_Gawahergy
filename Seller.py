from User import User
from Product import Product

class Seller(User):
    def __init__(self,name:str,password:str,email:str,id:int)->None:
        super().__init__(name,password,email)
        self.id = id
        self.products=[]

    def view_products(self):
        return self.products
    
    def add_products(self,Product)->None:
        self.products.append(Product)
    
    def select_product(self,products):
        name=input("\n Enter the Name of the Product you want")
        while True:
            selected_product = next((product for product in products if product.name == name), None)
            if selected_product:
                return selected_product
            else:
                print("\n There is no product with this name")
                name = input("\nWrite the name of your desired product: ")
        return

    def select_amount(self)->int:
        amount = int(input("\nHow many would you like to sell? "))
        while amount <= 0:
            print("\nThe amount should be greater than 0. Please, try again.")
            amount = int(input("\nHow many would you like to sell? "))
        return amount