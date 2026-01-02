class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age
    
    def grow(self):
        self.height += 6
    
    def age(self):
        self.plant_age += 6

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Days 1 ===")
    print(rose.get_info())
    rose.grow()
    rose.age()
    print("=== Day 7 ===")
    print(rose.get_info())
    print("Growth this week: +6cm")