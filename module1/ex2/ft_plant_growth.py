class Plant:
    """
    A class representing a plant that can grow and age.

    Attributes:
        name (str): The name of the plant.
        height (int): Current height in cm.
        plant_age (int): Current age in days.
    """

    def __init__(self, name: str, height: int, plant_age: int):
        """
        Initialize the plant.

        Args:
            name (str): Plant name.
            height (int): Initial height (cm).
            plant_age (int): Initial age (days).
        """
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, size: int = 1.0) -> None:
        """
        Increase the plant's height.

        Args:
            size (int, optional): Amount to grow in cm. Defaults to 1.0.
        """
        self.height += size

    def age(self, days: int = 1) -> None:
        """
        Increase the plant's age.

        Args:
            days (int, optional): Number of days to age. Defaults to 1.
        """
        self.plant_age += days

    def get_info(self) -> str:
        """
        Return a formatted string with plant details.

        Returns:
            str: Description of the plant's current state.
        """
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    rose.grow(6)
    rose.age(6)
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +6cm")
