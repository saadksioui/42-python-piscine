class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def get_info(self):
        return f"{self.name} ({self.height}cm, {self.plant_age} days)"
    
if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    print(f"Created: {rose.get_info()}")
    print(f"Created: {oak.get_info()}")
    print(f"Created: {cactus.get_info()}")
    print(f"Created: {sunflower.get_info()}")
    print(f"Created: {fern.get_info()}")
    print()
    print("Total plants created: 5")