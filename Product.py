class Product:
    def __init__(self, id, name, group, subgroup,price):
        self.id = id
        self.name = name
        self.group = group
        self.subgroup = subgroup
        self.price = price

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_group(self):
        return self.group

    def set_group(self, group):
        self.group = group
    
    def get_sub_group(self):
        return self.subgroup

    def set_sub_group(self, subgroup):
        self.subgroup = subgroup