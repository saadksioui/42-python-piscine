class Plant:
    """Base class for a generic plant."""
    
    def __init__(self, name: str, height: int):
        """Initialize plant name and height."""
        self.name = name
        self.height = height
    
    def grow(self) -> None:
        """Increase height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def describe(self) -> str:
        """Return plant description."""
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    """Class for plants that bloom."""
    
    def __init__(self, name: str, height: int, color: str):
        """Initialize with additional color attribute."""
        super().__init__(name, height)
        self.color = color
    
    def is_blooming(self) -> str:
        """Return blooming status."""
        return "(blooming)"
    
    def describe(self) -> str:
        """Override description to include flower details."""
        return f"{self.name}: {self.height}cm, {self.color} flowers {self.is_blooming()}"

class PrizeFlower(FloweringPlant):
    """Class for specialized prize-winning flowers."""
    
    def __init__(self, name: str, height: int, color: str, points: int):
        """Initialize with additional prize points."""
        super().__init__(name, height, color)
        self.points = points

    def describe(self) -> str:
        """Override description to include points."""
        return f"{super().describe()}, Prize points: {self.points}"

class GardenManager:
    """
    Manages garden operations and analytics.
    Demonstrates Class Methods and Nested Classes.
    """
    total_gardens = 0

    class GardenStats:
        """Nested helper class for calculating statistics."""
        
        def __init__(self):
            """Initialize stats counters."""
            self.plant_added = 0
            self.total_growth = 0
        
        def get_report(self) -> str:
            """Return formatted activity report."""
            return f"Plant added: {self.plant_added}, Total growth: {self.total_growth}cm"
        
        @staticmethod
        def calculate_score(plants: list) -> int:
            """
            Static method to calculate score based on plant attributes.
            Logic: Height + 15 (if Flower) + Points (if Prize).
            """
            score = 0
            for plant in plants:
                score += plant.height
                if hasattr(plant, "color"):
                    score += 15
                if hasattr(plant, "points"):
                    score += plant.points
            return score
                
    def __init__(self, owner: str):
        """Initialize manager for a specific owner."""
        self.owner = owner
        self.plants = []
        # Instantiate the nested class
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden and update stats."""
        self.plants.append(plant)
        self.stats.plant_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_plants(self) -> None:
        """Simulate growth for all plants."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def get_score(self) -> int:
        """Wrapper to calculate score using the nested stats class."""
        return self.stats.calculate_score(self.plants)

    def generate_report(self) -> None:
        """Generate and print full analysis."""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.describe()}")
        print()
        print(self.stats.get_report())
        
        # Count types using isinstance (OOP Best Practice: Check Child first)
        regular = 0
        flower = 0
        prize_flower = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prize_flower += 1
            elif isinstance(plant, FloweringPlant):
                flower += 1
            else:
                regular += 1
                
        print(f"Plant types: {regular} regular, {flower} flowering, {prize_flower} prize flowers")

    @classmethod
    def get_total_gardens(cls) -> str:
        """Class method to track global garden count."""
        return f"Total gardens managed: {cls.total_gardens}"
    
    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        """Factory class method to create multiple managers."""
        network = []
        for owner in owners:
            garden = cls(owner)
            network.append(garden)
        return network

    @staticmethod
    def validate_height(height: int) -> bool:
        """Static utility method for validation."""
        return height > 0

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
    print(f"Garden scores - {owner1.owner}: {owner1.stats.calculate_score(owner1.plants)}, {owner2.owner}: 92")
    print(GardenManager.get_total_gardens())