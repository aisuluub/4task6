class House:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.free_area = 0

    def add_furniture(self, **kwargs):
        self.free_area = self.area - sum(kwargs.values())
        print(f"Type: {self.name}")
        print(f"Free area---{self.free_area}")
        print(f"Total area---{self.area}")
        print(f"Furniture names: ",', '.join(kwargs.keys()))



house1 = House('Dom', 15)
house1.add_furniture(Bed=4, Wardrope=2, Table=1.5)
