# Animal Class in Python

This Python script demonstrates a simple implementation of a class called `Animal`. The class models a basic animal with two parameters `x` and `y` and provides methods for addition and multiplication of these parameters.

## Class Description

### `Animal`

The `Animal` class represents a simple model of an animal with two attributes `x` and `y`. The class provides methods for performing addition and multiplication on these attributes.

**Attributes:**
- `x`: The first parameter for operations, can be an `int` or `float`.
- `y`: The second parameter for operations, can be an `int` or `float`.
- `c`: A constant attribute set to the value `100`.

**Methods:**
- `__init__(x, y)`: Initializes an object of the `Animal` class with the given `x` and `y` values, and sets the attribute `c` to `100`.
- `slogeniya()`: Returns the sum of `x` and `y`.
- `umnogenniya()`: Returns the product of `x` and `y`.
- `__str__()`: Returns a string representation of the `Animal` class.

### Example Usage

```python
a = Animal(10, 10)

print(a.x)  # Output: 10
print(a.y)  # Output: 10
print(a.slogeniya())  # Output: 20
print(a.umnogenniya())  # Output: 100
print(a)  # Output: Class Animal
Additional Notes
The script also contains commented code showing how to define a basic class A with a method name that returns the name of the class.
The .replace() method is used for string manipulation.
Feel free to modify and expand the class according to your needs!

javascript


This `README.md` file gives an overview of the `Animal` class and its functionality