# Lesson 6 Independent Challenges

## Challenge 1A: `BankAccount`

There are two incomplete methods in this class, `deposit` and `withdraw`.

To complete `deposit`, you should raise a `ValueError` with the exact text below in the case where the deposit amount is not positive:

```
We only accept deposits of positive amounts.
```

Otherwise, you should add the amount to the account balance.

To complete `withdraw`, you should raise a `ValueError` with the exact text below in the case where the withdrawal amount is not positive:

```
We only accept withdrawals of positive amounts.
```

In the case where the withdrawal amount is greater than the account balance, you should raise a `ValueError` with the exact text below:

```
You cannot withdraw more than you have in your account.
```

Otherwise, you should subtract the amount from the account balance.

## Challenge 1B: `ATM`

Again, there are two incomplete methods in this class, `process_deposit` and `process_withdrawal`.

To complete `process_deposit`, you should first ask the user how much they would like to deposit into their account. If their response is not a valid number, print the exact text below:

```
That doesn't seem like a number.
```

Otherwise, attempt to deposit the amount into the account associated with the given account number. If an exception arises, print the exception text. Otherwise, print the following exact text, replacing `___` with the new account balance:

```
Your deposit was successful. Your new balance is ___. Thank you!
```

To complete `process_withdrawal`, you should first ask the user how much they would like to withdraw from their account. If their response is not a valid number, print the exact text below:

```
That doesn't seem like a number.
```

Otherwise, attempt to withdraw the amount from the account associated with the given account number. If an exception arises, print the exception text. Otherwise, print the following exact text, replacing `___` with the new account balance:

```
Your withdrawal was successful. Your new balance is ___. Thank you!
```

## Challenge 2A: `Animal`

There are four incomplete methods in this class.

To complete the `__init__` method, add each of the given parameters (name, age, species) to the `self`.

To complete the `__repr__` method, return a string of the exact format below, replacing the `<name>` with the animal's name, `<age>` with the animal's age, and `<species` with the animal's species:

```
<name>, <age> (<species>)
```

To complete the `__eq__` method, return a boolean value based on whether the `self` and the other animal have the same name, age and species.

To complete the `celebrate_birthday` method, increase the animal's age by one and print the following exact text, replacing `___` with the animal's name:

```
It's ___'s birthday.
```

## Challenge 2B: `Dog`

There are two incomplete methods in this class.

To complete the `__init__` method, you should call use the superclass `__init__` method, ensuring you set the species to `"dog"`.

To complete the `woof` method, you should print the exact text below, replacing `___` with the dog's name:

```
___ says woof!
```

## Challenge 2C: `Cat`

There are two incomplete methods in this class.

To complete the `__init__` method, you should call use the superclass `__init__` method, ensuring you set the species to `"cat"`.

To complete the `meow` method, you should print the exact text below, replacing `___` with the cat's name:

```
___ says meow!
```

## Challenge 2D: `PetShop`

There are five incomplete methods in this class.

To complete the `__init__` method, add the given parameter (pets) to the `self`.

To complete the `from_pet_dataset` method, return a new `PetShop` whose internal `pets` list is a list of animals from the given pet dataset.
For every animal in the pet dataset, if its species is `"dog"`, a `Dog` object should be created and added to the `pets` list, or if its species is `"cat"`, a `Cat` object should be added to the `pets` list.
If its species is neither of these, an `Animal` object should be added to the `pets` list.

To complete the `find_pet_with_name` method, return the first pet from the `pets` list that matches the given name, or if none match, raise a `ValueError` with the following exact text, replacing `___` with the given name:

```
No pets called ___ found in our shop.
```

To complete the `add_pet` method, add the given pet to the end of the `pets` list and print the following exact text, replacing `<name>` with the given pet's name and `<species>` with the given pet's species:

```
<name> the <species> is now looking for a new home.
```

To complete the `sell_pet` method, if the given pet is in the `pets` list, remove it and print the following exact text, replacing `<name>` with the given pet's name and `<species>` with the given pet's species:

```
<name> the <species> has found a new home.
```

Otherwise, print the following exact text, again replacing `<name>` with the given pet's name and `<species>` with the given pet's species:

```
<name> the <species> is not for sale in our shop.
```
