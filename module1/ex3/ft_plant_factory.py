class Plant:
    """
    A class representing a plant created by the factory.

    Attributes:
        name (str): The name of the plant.
        height (int): Initial height in cm.
        plant_age (int): Initial age in days.
    """

    def __init__(self, name: str, height: int, plant_age: int):
        """
        Initialize a new plant and announce its creation.

        Args:
            name (str): The name of the plant.
            height (int): Initial height in centimeters.
            plant_age (int): Initial age in days.
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age
        print(f"Created: {self.name} ({self.height}cm, {self.plant_age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)

    print("\nTotal plants created: 5")