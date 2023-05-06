class Cart:
    def __init__(self, id, products):
        self.id = id
        self.number_of_products = products
        #self.price = price
        #self.total = total

    def calculate_total(self):
        self.total=sum(self.products.price)
        return self.total



