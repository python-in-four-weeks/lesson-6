from typing import TypedDict


class PetData(TypedDict):
    name: str
    age: int
    species: str


pet_dataset: list[PetData] = [
    {"name": "Spot", "age": 5, "species": "dog"},
    {"name": "Fluffy", "age": 16, "species": "cat"},
    {"name": "Buddy", "age": 3, "species": "dog"},
    {"name": "Fido", "age": 9, "species": "dog"},
    {"name": "Nemo", "age": 1, "species": "fish"},
    {"name": "Ginger", "age": 8, "species": "cat"},
    {"name": "Floppy", "age": 2, "species": "rabbit"},
]


class Animal:
    def __init__(self, name: str, age: int, species: str):
        pass

    def __repr__(self):
        return ""

    def __eq__(self, other_animal):
        return False

    def celebrate_birthday(self) -> None:
        pass


class Dog(Animal):
    def __init__(self, name: str, age: int):
        pass

    def woof(self) -> None:
        pass


class Cat(Animal):
    def __init__(self, name: str, age: int):
        pass

    def meow(self) -> None:
        pass


class PetShop:
    def __init__(self, pets: list[Animal]):
        pass

    @classmethod
    def from_pet_dataset(cls, pet_dataset: list[PetData]):
        pass

    def find_pet_with_name(self, name: str) -> Animal:
        raise ValueError(f"No pets called {name} found in our shop.")

    def add_pet(self, pet: Animal) -> None:
        pass

    def sell_pet(self, pet: Animal) -> None:
        pass


if __name__ == "__main__":
    # Try out your functions here
    pet_shop = PetShop.from_pet_dataset(pet_dataset)
    pet_shop.pets[0].celebrate_birthday()
    pet_shop.sell_pet(pet_shop.pets[2])
