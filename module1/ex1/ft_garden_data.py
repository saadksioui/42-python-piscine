class Plant:
    """
    A class to represent a plant in the garden.

    Attributes:
        name (str): The name of the plant.
        height (int): The current height of the plant in cm.
        plant_age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, plant_age: int):
        """
        Initialize a new Plant instance with specific characteristics.

        Args:
            name (str): The name of the plant.
            height (int): Initial height in centimeters.
            plant_age (int): Initial age in days.
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sun_flower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.plant_age} days old")
    print(f"{sun_flower.name}: {sun_flower.height}cm, {sun_flower.plant_age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.plant_age} days old")