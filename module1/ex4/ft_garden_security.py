class SecurePlant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self._height = height
        self._plant_age = plant_age

    def get_height(self):
        return self._height
    
    def get_age(self):
        return self._plant_age
    
    def set_height(self, size: int):
        if size < 0:
            print(f"Invalid operation attempted: height {size}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = size
        print(f"Height updated: {size}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._plant_age = age
        print(f"Age updated: {age} days [OK]")

    def get_info(self):
        return f"Current plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)"
    
if __name__ == "__main__":
    rose = SecurePlant("Rose", 0, 0)
    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    print(rose.get_info())