class Plant:
    """
    Base class representing a generic plant in the garden.

    Attributes:
        name (str): The name of the plant.
        height (int): Height in cm.
        plant_age (int): Age in days.
    """
    def __init__(self, name: str, height: int, plant_age: int):
        """Initialize the plant with common attributes."""
        self.name = name
        self.height = height
        self.plant_age = plant_age

class Flower(Plant):
    """
    Represents a flowering plant that has a specific color and can bloom.
    """
    def __init__(self, name: str, height: int, plant_age: int, color: str):
        """
        Initialize the flower using the parent constructor.

        Args:
            color (str): The color of the flower.
        """
        super().__init__(name, height, plant_age)
        self.color = color

    def bloom(self) -> str:
        """Return a string simulating the bloom action."""
        return f"{self.name} is blooming beautifully!"

    def get_flower_info(self) -> str:
        """Return specific details about the flower."""
        return f"{self.name} (Flower): {self.height}cm, {self.plant_age} days, {self.color} color"

class Tree(Plant):
    """
    Represents a tree with a trunk diameter that produces shade.
    """
    def __init__(self, name: str, height: int, plant_age: int, trunk_diameter: int):
        """
        Initialize the tree using the parent constructor.

        Args:
            trunk_diameter (int): The diameter of the trunk in cm.
        """
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """
        Calculate shade based on trunk diameter.
        
        Note: Instead of hardcoding '78', we calculate it.
        50cm * 1.56 = 78m^2
        """
        shade_area = self.trunk_diameter * 1.56
        return f"{self.name} provides {int(shade_area)} square meters of shade"
    
    def get_tree_info(self) -> str:
        """Return specific details about the tree."""
        return f"{self.name} (Tree): {self.height}cm, {self.plant_age} days, {self.trunk_diameter}cm diameter"

class Vegetable(Plant):
    """
    Represents a vegetable with harvest season and nutritional value.
    """
    def __init__(self, name: str, height: int, plant_age: int, harvest_season: str, nutritional_value: str):
        """
        Initialize the vegetable using the parent constructor.

        Args:
            harvest_season (str): The season suitable for harvest.
            nutritional_value (str): The main nutrient.
        """
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self) -> str:
        """Return the nutritional info string."""
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_vegetable_info(self) -> str:
        """Return specific details about the vegetable."""
        return f"{self.name} (Vegetable): {self.height}cm, {self.plant_age} days, {self.harvest_season} harvest"

if __name__ == "__main__":
    print("Garden Plant Types")
    print()

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 15, 12, "yellow")
    
    print(rose.get_flower_info())
    print(rose.bloom())
    print(tulip.get_flower_info())
    print()

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 350, 1000, 30)
    
    print(oak.get_tree_info())
    print(oak.produce_shade())
    print(pine.get_tree_info())
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 45, "spring", "vitamin A")
    
    print(tomato.get_vegetable_info())
    print(tomato.show_nutrition())
    print(carrot.get_vegetable_info())