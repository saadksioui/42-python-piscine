class SecurePlant:
    """
    A class representing a plant with secure data access.

    Attributes:
        name (str): The name of the plant.
        _height (int): Protected height in cm.
        _plant_age (int): Protected age in days.
    """

    def __init__(self, name: str, height: int, plant_age: int):
        """
        Initialize the secure plant and validate initial data.

        Args:
            name (str): Name of the plant.
            height (int): Initial height.
            plant_age (int): Initial age.
        """
        self.name = name
        # Initialize protected attributes directly first
        self._height = 0.0
        self._plant_age = 0
        
        print(f"Plant created: {self.name}")
        
        # Use setters to validate and set initial values
        self.set_height(height)
        self.set_age(plant_age)

    def get_height(self) -> int:
        """
        Safely retrieve the plant's height.

        Returns:
            int: Current height in cm.
        """
        return self._height
    
    def get_age(self) -> int:
        """
        Safely retrieve the plant's age.

        Returns:
            int: Current age in days.
        """
        return self._plant_age
    
    def set_height(self, value: int) -> None:
        """
        Securely update the plant's height with validation.

        Args:
            value (int): New height value. Must be non-negative.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """
        Securely update the plant's age with validation.

        Args:
            value (int): New age value. Must be non-negative.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._plant_age = value
            print(f"Age updated: {value} days [OK]")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    print(f"\nCurrent plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")