class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

class Flower(Plant):
    def __init__(self, name: str, height: int, plant_age: int, color: str):
        super().__init__(name, height, plant_age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"
    
    def get_flower_info(self):
        return f"{self.name} (Flower): {self.height}cm, {self.plant_age} days, {self.color} color"

class Tree(Plant):
    def __init__(self, name: str, height: int, plant_age: int, trunk_diameter: int):
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        return f"{self.name} provides 78 square meters of shade"

    def get_tree_info(self):
        return f"{self.name} (Tree): {self.height}cm, {self.plant_age} days, {self.trunk_diameter}cm diameter"

class Vegetable(Plant):
    def __init__(self, name: str, height: int, plant_age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition_type(self):
        return f"{self.name} is rich in {self.nutritional_value}"
    
    def get_vegetable_info(self):
        return f"{self.name} (Vegetable): {self.height}cm, {self.plant_age} days, {self.harvest_season} harvest"

if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===")
    print()
    print(rose.get_flower_info())
    print(rose.bloom())
    print()
    print(oak.get_tree_info())
    print(oak.produce_shade())
    print()
    print(tomato.get_vegetable_info())
    print(tomato.nutrition_type())