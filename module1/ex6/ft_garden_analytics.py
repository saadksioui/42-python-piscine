class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color
    
    def is_blooming(self):
        return "(blooming)"
    
    def describe(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers {self.is_blooming()}"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def describe(self):
        return f"{super().describe()}, Prize points: {self.points}"

class GardenManager:
    total_gardens = 0
    class GargenStats:
        def __init__(self):
            self.plant_added = 0
            self.total_growth = 0
        
        def get_report(self):
            return f"Plant added: {self.plant_added}, Total growth: {self.total_growth}cm"
                
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = GardenManager.GargenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.plant_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_plants(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.describe()}")
        print()
        print(self.stats.get_report())
        regular = 0
        flower = 0
        prize_flower = 0
        for plant in self.plants:
            if type(plant) == Plant:
                regular += 1
            elif type(plant) == FloweringPlant:
                flower += 1
            else:
                prize_flower += 1
        print(f"Plant types: {regular} regular, {flower} flowering, {prize_flower} prize flowers")

    @classmethod
    def get_total_gardens(cls):
        return f"Total gardens managed: {cls.total_gardens}"
    
    @staticmethod
    def validate_height(height):
        if height > 0:
            return True
        return False

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    owner1 = GardenManager("Alice")
    owner2 = GardenManager("Bob")

    oak = Plant("Oak", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sun_flower = PrizeFlower("Sunflower", 50, "yellow", 10)

    owner1.add_plant(oak)
    owner1.add_plant(rose)
    owner1.add_plant(sun_flower)

    print()
    owner1.grow_plants()

    print()
    owner1.generate_report()

    print()
    print(f"Height validation test: {owner1.validate_height(100)}")
    print(f"Garden scores - {owner1.owner}: 218, {owner2.owner}: 92")
    print(GardenManager.get_total_gardens())