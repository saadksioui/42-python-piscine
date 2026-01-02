class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
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