import pytest
from pytest_mock import MockerFixture

from io import StringIO

import bank_challenges
import pet_shop_challenges


@pytest.mark.parametrize(
    "account_number, customer_name, initial_balance, deposit_amount, final_balance",
    [
        ("12169553", "Alice Smith", 50, 30, 80),
        ("82309802", "Bob Jones", 200, 12, 212),
    ],
)
def test_bank_account_with_valid_deposit(
    account_number: str,
    customer_name: str,
    initial_balance: float,
    deposit_amount: float,
    final_balance: float,
) -> None:
    bank_account = bank_challenges.BankAccount(
        account_number, customer_name, initial_balance
    )
    bank_account.deposit(deposit_amount)
    assert (
        bank_account.balance == final_balance
    ), f"A bank account with {initial_balance} initial balance should contain {final_balance} after a deposit of {deposit_amount}"


@pytest.mark.parametrize(
    "account_number, customer_name, initial_balance, deposit_amount, expected_error_message",
    [
        (
            "12169553",
            "Alice Smith",
            50,
            0,
            "We only accept deposits of positive amounts.",
        ),
        (
            "82309802",
            "Bob Jones",
            200,
            -10,
            "We only accept deposits of positive amounts.",
        ),
    ],
)
def test_bank_account_with_invalid_deposit(
    account_number: str,
    customer_name: str,
    initial_balance: float,
    deposit_amount: float,
    expected_error_message: str,
) -> None:
    bank_account = bank_challenges.BankAccount(
        account_number, customer_name, initial_balance
    )
    with pytest.raises(ValueError) as error:
        bank_account.deposit(deposit_amount)
    assert (
        str(error.value) == expected_error_message
    ), f'Trying to deposit {deposit_amount} should raise error with message "{expected_error_message}"'
    assert (
        bank_account.balance == initial_balance
    ), "Failed deposit should not affect balance"


@pytest.mark.parametrize(
    "account_number, customer_name, initial_balance, withdrawal_amount, final_balance",
    [
        ("12169553", "Alice Smith", 50, 30, 20),
        ("82309802", "Bob Jones", 200, 12, 188),
    ],
)
def test_bank_account_with_valid_withdrawal(
    account_number: str,
    customer_name: str,
    initial_balance: float,
    withdrawal_amount: float,
    final_balance: float,
) -> None:
    bank_account = bank_challenges.BankAccount(
        account_number, customer_name, initial_balance
    )
    bank_account.withdraw(withdrawal_amount)
    assert (
        bank_account.balance == final_balance
    ), f"A bank account with {initial_balance} initial balance should contain {final_balance} after a withdrawal of {withdrawal_amount}"


@pytest.mark.parametrize(
    "account_number, customer_name, initial_balance, withdrawal_amount, expected_error_message",
    [
        (
            "12169553",
            "Alice Smith",
            50,
            0,
            "We only accept withdrawals of positive amounts.",
        ),
        (
            "82309802",
            "Bob Jones",
            200,
            -10,
            "We only accept withdrawals of positive amounts.",
        ),
        (
            "38987723",
            "Charlie Taylor",
            100,
            1000000,
            "You cannot withdraw more than you have in your account.",
        ),
    ],
)
def test_bank_account_with_invalid_withdrawal(
    account_number: str,
    customer_name: str,
    initial_balance: float,
    withdrawal_amount: float,
    expected_error_message: str,
) -> None:
    bank_account = bank_challenges.BankAccount(
        account_number, customer_name, initial_balance
    )
    with pytest.raises(ValueError) as error:
        bank_account.withdraw(withdrawal_amount)
    assert (
        str(error.value) == expected_error_message
    ), f'Trying to withdraw {withdrawal_amount} should raise error with message "{expected_error_message}"'
    assert (
        bank_account.balance == initial_balance
    ), "Failed withdrawal should not affect balance"


@pytest.mark.parametrize(
    "account_number, deposit_amount_input, expected_success_message",
    [
        (
            "12169553",
            "30",
            "Your deposit was successful. Your new balance is 80.0. Thank you!",
        ),
        (
            "82309802",
            "12",
            "Your deposit was successful. Your new balance is 212.0. Thank you!",
        ),
    ],
)
def test_atm_process_deposit_with_valid_input(
    mocker: MockerFixture,
    account_number: str,
    deposit_amount_input: str,
    expected_success_message: str,
) -> None:
    atm = bank_challenges.ATM.from_account_dataset(bank_challenges.account_dataset)
    mocker.patch("builtins.input", side_effect=[deposit_amount_input])
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    atm.process_deposit(account_number)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_success_message
    ), f'Deposit of {deposit_amount_input} should generate success message "{expected_success_message}"'


@pytest.mark.parametrize(
    "account_number, deposit_amount_input, expected_error_message",
    [
        ("12169553", "hello", "That doesn't seem like a number."),
        ("82309802", "0", "We only accept deposits of positive amounts."),
        ("38987723", "-20", "We only accept deposits of positive amounts."),
    ],
)
def test_atm_process_deposit_with_invalid_input(
    mocker: MockerFixture,
    account_number: str,
    deposit_amount_input: str,
    expected_error_message: str,
) -> None:
    atm = bank_challenges.ATM.from_account_dataset(bank_challenges.account_dataset)
    mocker.patch("builtins.input", side_effect=[deposit_amount_input])
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    atm.process_deposit(account_number)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_error_message
    ), f'Deposit of {deposit_amount_input} should generate error message "{expected_error_message}"'


@pytest.mark.parametrize(
    "account_number, withdrawal_amount_input, expected_success_message",
    [
        (
            "12169553",
            "30",
            "Your withdrawal was successful. Your new balance is 20.0. Thank you!",
        ),
        (
            "82309802",
            "12",
            "Your withdrawal was successful. Your new balance is 188.0. Thank you!",
        ),
    ],
)
def test_atm_process_withdrawal_with_valid_input(
    mocker: MockerFixture,
    account_number: str,
    withdrawal_amount_input: str,
    expected_success_message: str,
) -> None:
    atm = bank_challenges.ATM.from_account_dataset(bank_challenges.account_dataset)
    mocker.patch("builtins.input", side_effect=[withdrawal_amount_input])
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    atm.process_withdrawal(account_number)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_success_message
    ), f'Withdrawal of {withdrawal_amount_input} should generate success message "{expected_success_message}"'


@pytest.mark.parametrize(
    "account_number, withdrawal_amount_input, expected_error_message",
    [
        ("12169553", "hello", "That doesn't seem like a number."),
        ("82309802", "0", "We only accept withdrawals of positive amounts."),
        ("38987723", "-20", "We only accept withdrawals of positive amounts."),
        (
            "32605081",
            "1000000",
            "You cannot withdraw more than you have in your account.",
        ),
    ],
)
def test_atm_process_withdrawal_with_invalid_input(
    mocker: MockerFixture,
    account_number: str,
    withdrawal_amount_input: str,
    expected_error_message: str,
) -> None:
    atm = bank_challenges.ATM.from_account_dataset(bank_challenges.account_dataset)
    mocker.patch("builtins.input", side_effect=[withdrawal_amount_input])
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    atm.process_withdrawal(account_number)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_error_message
    ), f"Deposit of {withdrawal_amount_input} should generate error message {expected_error_message}"


@pytest.mark.parametrize(
    "name, age, species",
    [
        ("Spot", 5, "dog"),
        ("Fluffy", 16, "cat"),
    ],
)
def test_animal_init(name: str, age: int, species: str) -> None:
    animal = pet_shop_challenges.Animal(name, age, species)
    assert animal.name == name
    assert animal.age == age
    assert animal.species == species


@pytest.mark.parametrize(
    "name, age, species",
    [
        ("Spot", 5, "dog"),
        ("Fluffy", 16, "cat"),
    ],
)
def test_animal_repr(name: str, age: int, species: str) -> None:
    animal = pet_shop_challenges.Animal(name, age, species)
    assert str(animal) == f"{name}, {age} ({species})"


@pytest.mark.parametrize(
    "animal_1, animal_2, should_be_equal",
    [
        (
            pet_shop_challenges.Dog(name="Spot", age=5),
            pet_shop_challenges.Dog(name="Spot", age=5),
            True,
        ),
        (
            pet_shop_challenges.Dog(name="Spot", age=5),
            pet_shop_challenges.Dog(name="Fido", age=9),
            False,
        ),
    ],
)
def test_animal_eq(
    animal_1: pet_shop_challenges.Animal,
    animal_2: pet_shop_challenges.Animal,
    should_be_equal: bool,
) -> None:
    is_equal = animal_1 == animal_2
    assert (
        is_equal == should_be_equal
    ), f"{animal_1} and {animal_2} are {'' if should_be_equal else 'not '}the same"


@pytest.mark.parametrize(
    "name, age, species, birthday_message",
    [
        ("Spot", 5, "dog", "It's Spot's birthday."),
        ("Fluffy", 16, "cat", "It's Fluffy's birthday."),
    ],
)
def test_animal_celebrate_birthday(
    mocker: MockerFixture, name: str, age: int, species: str, birthday_message: str
) -> None:
    animal = pet_shop_challenges.Animal(name, age, species)
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    animal.celebrate_birthday()
    assert animal.age == age + 1
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == birthday_message
    ), f'Birthday celebration method should print message "{birthday_message}"'


@pytest.mark.parametrize(
    "name, age",
    [
        ("Spot", 5),
        ("Fido", 9),
    ],
)
def test_dog_init(name: str, age: int) -> None:
    dog = pet_shop_challenges.Dog(name, age)
    assert dog.name == name
    assert dog.age == age
    assert dog.species == "dog"


@pytest.mark.parametrize(
    "name, age, woof_message",
    [
        ("Spot", 5, "Spot says woof!"),
        ("Fido", 9, "Fido says woof!"),
    ],
)
def test_dog_woof(
    mocker: MockerFixture, name: str, age: int, woof_message: str
) -> None:
    dog = pet_shop_challenges.Dog(name, age)
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    dog.woof()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == woof_message
    ), f'Woof method should print message "{woof_message}"'


@pytest.mark.parametrize(
    "name, age",
    [
        ("Fluffy", 16),
        ("Ginger", 8),
    ],
)
def test_cat_init(name: str, age: int) -> None:
    cat = pet_shop_challenges.Cat(name, age)
    assert cat.name == name
    assert cat.age == age
    assert cat.species == "cat"


@pytest.mark.parametrize(
    "name, age, meow_message",
    [
        ("Fluffy", 16, "Fluffy says meow!"),
        ("Ginger", 8, "Ginger says meow!"),
    ],
)
def test_cat_meow(
    mocker: MockerFixture, name: str, age: int, meow_message: str
) -> None:
    cat = pet_shop_challenges.Cat(name, age)
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    cat.meow()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == meow_message
    ), f'Meow method should print message "{meow_message}"'


@pytest.mark.parametrize(
    "pets",
    [
        [
            pet_shop_challenges.Dog(name="Spot", age=5),
            pet_shop_challenges.Cat(name="Fluffy", age=16),
            pet_shop_challenges.Cat(name="Ginger", age=8),
            pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
        ],
        [
            pet_shop_challenges.Dog(name="Buddy", age=3),
            pet_shop_challenges.Dog(name="Fido", age=9),
            pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
        ],
    ],
)
def test_pet_shop_init(pets: list[pet_shop_challenges.Animal]) -> None:
    pet_shop = pet_shop_challenges.PetShop(pets)
    assert pet_shop.pets == pets


@pytest.mark.parametrize(
    "pet_dataset, expected_pets",
    [
        (
            [
                {"name": "Spot", "age": 5, "species": "dog"},
                {"name": "Fluffy", "age": 16, "species": "cat"},
                {"name": "Ginger", "age": 8, "species": "cat"},
                {"name": "Floppy", "age": 2, "species": "rabbit"},
            ],
            [
                pet_shop_challenges.Dog(name="Spot", age=5),
                pet_shop_challenges.Cat(name="Fluffy", age=16),
                pet_shop_challenges.Cat(name="Ginger", age=8),
                pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
            ],
        ),
        (
            [
                {"name": "Buddy", "age": 3, "species": "dog"},
                {"name": "Fido", "age": 9, "species": "dog"},
                {"name": "Nemo", "age": 1, "species": "fish"},
            ],
            [
                pet_shop_challenges.Dog(name="Buddy", age=3),
                pet_shop_challenges.Dog(name="Fido", age=9),
                pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
            ],
        ),
    ],
)
def test_pet_shop_from_pet_dataset(
    pet_dataset: list[pet_shop_challenges.PetData],
    expected_pets: list[pet_shop_challenges.Animal],
) -> None:
    pet_shop = pet_shop_challenges.PetShop.from_pet_dataset(pet_dataset)
    assert pet_shop.pets == expected_pets


@pytest.mark.parametrize(
    "pet_shop, name, expected_pet",
    [
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Spot", age=5),
                    pet_shop_challenges.Cat(name="Fluffy", age=16),
                    pet_shop_challenges.Cat(name="Ginger", age=8),
                    pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
                ]
            ),
            "Ginger",
            pet_shop_challenges.Cat(name="Ginger", age=8),
        ),
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Buddy", age=3),
                    pet_shop_challenges.Dog(name="Fido", age=9),
                    pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
                ]
            ),
            "Nemo",
            pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
        ),
    ],
)
def test_pet_shop_find_pet_with_name_where_pet_in_shop(
    pet_shop: pet_shop_challenges.PetShop,
    name: str,
    expected_pet: pet_shop_challenges.Animal,
) -> None:
    pet = pet_shop.find_pet_with_name(name)
    assert pet == expected_pet, f"Expected to find {expected_pet}"


@pytest.mark.parametrize(
    "pet_shop, name, expected_error_message",
    [
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Spot", age=5),
                    pet_shop_challenges.Cat(name="Fluffy", age=16),
                    pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
                ]
            ),
            "Ginger",
            "No pets called Ginger found in our shop.",
        ),
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Buddy", age=3),
                    pet_shop_challenges.Dog(name="Fido", age=9),
                ]
            ),
            "Nemo",
            "No pets called Nemo found in our shop.",
        ),
    ],
)
def test_pet_shop_find_pet_with_name_where_pet_not_in_shop(
    pet_shop: pet_shop_challenges.PetShop, name: str, expected_error_message: str
) -> None:
    with pytest.raises(ValueError) as error:
        pet_shop.find_pet_with_name(name)
    assert (
        str(error.value) == expected_error_message
    ), f"Trying to find missing pet should give error message {expected_error_message}"


@pytest.mark.parametrize(
    "pet_shop, pet",
    [
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Spot", age=5),
                    pet_shop_challenges.Cat(name="Fluffy", age=16),
                    pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
                ]
            ),
            pet_shop_challenges.Cat(name="Ginger", age=8),
        ),
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Buddy", age=3),
                    pet_shop_challenges.Dog(name="Fido", age=9),
                ]
            ),
            pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
        ),
    ],
)
def test_pet_shop_add_pet(
    pet_shop: pet_shop_challenges.PetShop, pet: pet_shop_challenges.Animal
) -> None:
    original_pet_count = len(pet_shop.pets)
    pet_shop.add_pet(pet)
    assert (
        len(pet_shop.pets) == original_pet_count + 1
    ), f"Expected pet shop to contain one more pet than before"
    assert pet in pet_shop.pets, f"Expected {pet} to be in pet shop after adding"


@pytest.mark.parametrize(
    "pet_shop, pet, expected_message",
    [
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Spot", age=5),
                    pet_shop_challenges.Cat(name="Fluffy", age=16),
                    pet_shop_challenges.Cat(name="Ginger", age=8),
                    pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
                ]
            ),
            pet_shop_challenges.Cat(name="Ginger", age=8),
            "Ginger the cat has found a new home.",
        ),
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Buddy", age=3),
                    pet_shop_challenges.Dog(name="Fido", age=9),
                    pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
                ]
            ),
            pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
            "Nemo the fish has found a new home.",
        ),
    ],
)
def test_pet_shop_sell_pet_with_pet_in_shop(
    mocker: MockerFixture,
    pet_shop: pet_shop_challenges.PetShop,
    pet: pet_shop_challenges.Animal,
    expected_message: str,
) -> None:
    original_pet_count = len(pet_shop.pets)
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    pet_shop.sell_pet(pet)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert (
        len(pet_shop.pets) == original_pet_count - 1
    ), f"Expected pet shop to contain one less pet than before"
    assert (
        pet not in pet_shop.pets
    ), f"Expected {pet} not to be in pet shop after removal"
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_message
    ), f'Successful sale should print message "{expected_message}"'


@pytest.mark.parametrize(
    "pet_shop, pet, expected_message",
    [
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Spot", age=5),
                    pet_shop_challenges.Cat(name="Fluffy", age=16),
                    pet_shop_challenges.Animal(name="Floppy", age=2, species="rabbit"),
                ]
            ),
            pet_shop_challenges.Cat(name="Ginger", age=8),
            "Ginger the cat is not for sale in our shop.",
        ),
        (
            pet_shop_challenges.PetShop(
                [
                    pet_shop_challenges.Dog(name="Buddy", age=3),
                    pet_shop_challenges.Dog(name="Fido", age=9),
                ]
            ),
            pet_shop_challenges.Animal(name="Nemo", age=1, species="fish"),
            "Nemo the fish is not for sale in our shop.",
        ),
    ],
)
def test_pet_shop_sell_pet_with_pet_not_in_shop(
    mocker: MockerFixture,
    pet_shop: pet_shop_challenges.PetShop,
    pet: pet_shop_challenges.Animal,
    expected_message: str,
) -> None:
    original_pet_count = len(pet_shop.pets)
    mock_stdout = mocker.patch("sys.stdout", new_callable=StringIO)
    pet_shop.sell_pet(pet)
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert (
        len(pet_shop.pets) == original_pet_count
    ), f"Expected pet shop to contain same number of pets as before"
    assert pet not in pet_shop.pets, f"Expected {pet} not to be in pet shop"
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert (
        outputted_lines[-1] == expected_message
    ), f'Absent pet should print message "{expected_message}"'
