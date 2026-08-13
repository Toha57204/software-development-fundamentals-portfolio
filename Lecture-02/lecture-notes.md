# Lecture 02 Notes - Data Types, Variables, Operators, Expressions and Libraries

## 1. Data Types

A data type tells the computer how a value should be interpreted and used.

Different types of data can represent different kinds of information.

Common data types discussed in this lesson include:

- Integer
- Floating-point
- Double precision
- Decimal
- Character
- Boolean
- String
- Byte

Python determines the type of a value from the value that is assigned.

---

# 2. Integer

Integers are whole numbers with no fractional part.

In Python, integers use the `int` type.

Examples:

```python
534
2
7903
-45
```

These are not integers:

```text
5.49
"VIT"
88.0
```

Integers are useful for:

- Counts
- Indexes
- Exact whole-number values

---

# 3. Floating-Point Numbers

Floating-point numbers represent numbers containing a decimal point or fractional part.

Examples:

```python
534.8
2.0
7903.97283
45.1
```

Python uses floating-point values when a decimal value is required.

---

# 4. Double Precision

Double precision provides:

- More range
- More precision
- Greater memory usage

It is useful when calculations require larger values or greater accuracy.

Typical double-precision values provide around 15–16 significant digits.

---

# 5. Decimal Precision

Decimal values are useful when exact decimal behaviour is important.

A common example is financial calculations.

Decimal values can provide high precision for calculations where significant digits matter.

---

# 6. Characters

A character represents one symbol.

Examples:

```text
'B'
'd'
'4'
'$'
'\n'
```

Special character sequences such as:

```text
\n
```

can represent special characters such as a new line.

---

# 7. Boolean Values

Boolean values represent:

```python
True
False
```

They are commonly used to represent the result of a condition.

Examples:

```python
a > b
a == 1
```

These expressions return either:

```python
True
```

or:

```python
False
```

---

# 8. Strings

Strings store text as a sequence of characters.

Examples:

```python
"Victorian Institute of Technology"
"VIT"
"89.324"
```

Even though:

```python
"89.324"
```

contains numbers, quotation marks make it text.

---

# 9. Byte Values

The lesson describes byte values as ranging from:

```text
0 to 255
```

Valid examples:

```text
10
5
255
```

Invalid examples:

```text
-1
256
1000
```

---

# 10. Variables

A variable gives a readable name to a stored value.

Example:

```python
monthly_salary = 25
```

The variable name refers to the value stored in memory.

Using meaningful variable names makes programs easier to understand.

---

# 11. Variable Naming Rules

Python variable names should:

1. Start with a letter or underscore
2. Contain letters, digits or underscores
3. Not contain spaces
4. Not contain periods
5. Not use Python reserved words

Good examples:

```python
student_name
score2
total
```

Invalid examples:

```text
7times
here.there
there+goes
a%b
for
```

Python is case-sensitive.

Therefore:

```python
total
Total
TOTAL
```

are different variable names.

---

# 12. Assigning Values

Python does not require a separate declaration before assigning a value.

Example:

```python
name = "xyz"
weight = 62.8
height = 168
```

Python infers the data type from the assigned value.

Here:

```text
name   → string
weight → floating-point
height → integer
```

---

# 13. Converting Values to Integers

The `int()` function converts a value to an integer.

Example:

```python
weight = int(68.2)
height = int(175.7)
```

Results:

```text
68
175
```

The decimal portion is removed.

The conversion truncates the fractional part rather than rounding it.

---

# 14. Expressions

An expression combines operands and operators to produce a result.

Example:

```python
8 * 9
```

Result:

```text
72
```

Variables can also be used as operands.

Example:

```python
x = 8 * y
z = x - 13
x = x + 1
```

---

# 15. Types of Expressions

Three important types of expressions are:

## Mathematical Expression

Used to calculate a value.

```python
8 * 9
```

## Comparison Expression

Used to test a relationship.

```python
x > y
```

## Logical Expression

Used to combine conditions.

```python
ready and paid
```

---

# 16. Mathematical Operators

Python mathematical operators include:

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Remainder |

Examples:

```python
5 + 2
5 - 2
5 * 2
5 / 2
5 % 2
```

---

# 17. Division

The division operator is:

```text
/
```

Example:

```python
5.0 / 2
```

Result:

```text
2.5
```

Division produces a quotient.

---

# 18. Remainder Operator

The remainder operator is:

```text
%
```

It returns what remains after division.

Example:

```python
7.0 % 3.0
```

Result:

```text
1
```

Another example:

```python
12.0 % 3.0
```

Result:

```text
0
```

---

# 19. Unary Operators

Unary operators operate on one value.

Examples:

```text
+
-
```

Unary plus:

```python
+7.2
```

Unary minus:

```python
-7.2
```

If no sign is written, a numeric value is positive by default.

---

# 20. Increment and Decrement

Python increases a value using:

```python
count += 1
```

This means:

```python
count = count + 1
```

Python decreases a value using:

```python
count -= 1
```

This means:

```python
count = count - 1
```

Python does not normally use:

```text
++
--
```

like some other programming languages.

---

# 21. Operator Precedence

Operators are evaluated in a particular order.

The lesson introduces this order:

1. Parentheses
2. Unary operations
3. Multiplication, division and remainder
4. Addition and subtraction

Example:

```python
2 + 3 * 4
```

Multiplication happens first:

```text
3 * 4 = 12
```

Then:

```text
2 + 12 = 14
```

Result:

```text
14
```

Parentheses can change the order.

Example:

```python
(2 + 3) * 4
```

Result:

```text
20
```

Operators at the same level are evaluated from left to right.

---

# 22. Comparison Operators

Comparison operators test relationships.

| Operator | Meaning |
|---|---|
| `<` | Less than |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `!=` | Not equal to |

Every comparison produces either:

```python
True
```

or:

```python
False
```

---

# 23. Comparison Examples

Suppose:

```python
A = 5
B = 3
```

Then:

```python
A > B
```

Result:

```python
True
```

If:

```python
A = 5
B = 7
```

then:

```python
A > B
```

Result:

```python
False
```

---

# 24. Turning Questions into Comparisons

Question:

```text
Is X bigger than Y?
```

Python:

```python
X > Y
```

Question:

```text
Is Y at least Z?
```

Python:

```python
Y >= Z
```

Question:

```text
Are X and Z the same?
```

Python:

```python
X == Z
```

---

# 25. Logical Operators

Python has three important logical operators:

```python
and
or
not
```

---

# 26. Logical AND

The `and` operator requires both conditions to be `True`.

Example:

```python
(year12 == "Yes") and (ielts > 6)
```

The result is `True` only when both conditions are true.

---

# 27. Logical OR

The `or` operator requires at least one condition to be `True`.

Example:

```python
(farecard == "Yes") or (cash > 2)
```

The result is `False` only when both conditions are false.

---

# 28. Logical NOT

The `not` operator reverses a Boolean value.

Example:

```python
not True
```

Result:

```python
False
```

Example:

```python
not False
```

Result:

```python
True
```

---

# 29. Libraries and Methods

Libraries organise reusable programming functionality.

A general method call can be written as:

```text
result = ClassName.method_name(argument1, argument2)
```

Important parts include:

- Class name
- Method name
- Arguments
- Return value

When calling a method, it is important to check:

- Method name
- Return type
- Number of arguments
- Argument types
- Argument order

---

# 30. Python Math Library

Python provides the `math` module for mathematical operations.

Import the library:

```python
import math
```

Calculate a square root:

```python
root = math.sqrt(25)
```

Calculate a power:

```python
power = math.pow(2, 3)
```

The `math` module provides reusable mathematical functions including:

- Square roots
- Powers
- Trigonometric calculations
- Other mathematical operations

---

# Example

```python
import math

name = "VIT"
score = 75
weight = 62.8

print(name)
print(score)
print(weight)

print(score > 50)

root = math.sqrt(25)
power = math.pow(2, 3)

print(root)
print(power)
```

---

# Quick Reference

| Concept | Example |
|---|---|
| Integer | `10` |
| Float | `10.5` |
| String | `"VIT"` |
| Boolean | `True` |
| Variable | `score = 75` |
| Integer conversion | `int(68.2)` |
| Addition | `x + y` |
| Subtraction | `x - y` |
| Multiplication | `x * y` |
| Division | `x / y` |
| Remainder | `x % y` |
| Equal | `x == y` |
| Not equal | `x != y` |
| Greater than | `x > y` |
| Less than | `x < y` |
| Logical AND | `and` |
| Logical OR | `or` |
| Logical NOT | `not` |
| Square root | `math.sqrt()` |
| Power | `math.pow()` |

---

# Key Takeaways

- Data types give values meaning.
- Variables name and store values.
- Python infers variable types from assigned values.
- Expressions combine operands and operators.
- Mathematical operators perform calculations.
- Comparison operators return `True` or `False`.
- Logical operators combine conditions.
- Operator precedence controls calculation order.
- Libraries provide reusable functionality.
- Python's `math` module provides useful mathematical functions.
