# Lecture 02 Notes - Data Types, Variables, Operators, Expressions and Libraries

## 1. Data Types

A data type tells the computer how a value should be interpreted and used.

Types covered in this lesson include:

- Integer
- Floating-point
- Double precision
- Decimal
- Character
- Boolean
- String
- Byte

Python determines the type of a value from the value assigned to it.

---

## 2. Integer

Integers are whole numbers with no fractional part.

In Python, integers use the `int` type.

Examples:

```python
534
2
7903
-45
```

Not integers:

```text
5.49
"VIT"
88.0
```

Integers are useful for counts, indexes and exact whole-number values.

---

## 3. Floating-Point Numbers

Floating-point numbers represent values containing a decimal point or fractional part.

Examples:

```python
534.8
2.0
7903.97283
45.1
```

---

## 4. Double Precision

Double precision provides:

- More range
- More precision
- More memory usage

It is useful when calculations require greater accuracy.

The lesson describes typical double precision as about 15–16 significant digits.

---

## 5. Decimal Precision

Decimal values are useful when exact decimal behaviour is important.

A common example is financial calculations.

---

## 6. Characters

A character represents one symbol.

Examples:

```text
'B'
'd'
'4'
'$'
'\n'
```

Escape sequences such as:

```text
\n
```

represent special characters.

---

## 7. Boolean Values

Boolean values are:

```python
True
False
```

They are commonly produced by conditions.

Examples:

```python
a > b
a == 1
```

A comparison produces either `True` or `False`.

---

## 8. Strings

Strings store text as a sequence of characters.

Examples:

```python
"Victorian Institute of Technology"
"VIT"
"89.324"
```

Even though `"89.324"` contains digits, it is still text because it is inside quotation marks.

---

## 9. Byte Values

The lesson describes byte values as ranging from:

```text
0 to 255
```

Valid:

```text
10
5
255
```

Invalid:

```text
-1
256
1000
```

---

## 10. Variables

A variable gives a readable name to a value stored in memory.

Example:

```python
monthly_salary = 25
```

Meaningful variable names make programs easier to understand.

---

## 11. Variable Naming Rules

A Python variable should:

1. Start with a letter or underscore
2. Use letters, numbers and underscores
3. Not contain spaces
4. Not contain periods
5. Not use Python reserved words

Valid examples:

```python
donald
donald_trump
integer
times7
street_forty_three
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

## 12. Assigning Values

Python does not require a separate variable declaration.

Example:

```python
name = "xyz"
weight = 62.8
height = 168
```

Python infers the type from the assigned value.

- `name` → string
- `weight` → float
- `height` → integer

---

## 13. Converting to Integer

Use `int()` when you intentionally want an integer value.

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

The fractional part is removed.

The conversion truncates rather than rounds.

---

## 14. Expressions

An expression combines operands and operators to produce a result.

Example:

```python
8 * 9
```

Result:

```text
72
```

Variables can also be used as operands:

```python
x = 8 * y
z = x - 13
x = x + 1
```

---

## 15. Kinds of Expressions

### Mathematical

Used to calculate a value.

```python
8 * 9
```

### Comparison

Used to test a relationship.

```python
x > y
```

### Logical

Used to combine conditions.

```python
ready and paid
```

---

## 16. Mathematical Operators

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Remainder |

Examples:

```python
10 + 5
10 - 5
10 * 5
10 / 5
10 % 3
```

---

## 17. Division

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

---

## 18. Remainder

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

## 19. Unary Operators

Unary operators work with one operand.

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

## 20. Increment and Decrement

Increase a value by one:

```python
count += 1
```

This is equivalent to:

```python
count = count + 1
```

Decrease a value by one:

```python
count -= 1
```

Python uses `+= 1` and `-= 1` rather than the `++` and `--` notation used by some other languages.

---

## 21. Operator Precedence

The lesson introduces this evaluation order:

1. Parentheses
2. Unary operations
3. `*`, `/`, `%`
4. `+`, `-`

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

Using parentheses:

```python
(2 + 3) * 4
```

Result:

```text
20
```

Operators at the same level are evaluated from left to right.

---

## 22. Comparison Operators

| Operator | Meaning |
|---|---|
| `<` | Less than |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `!=` | Not equal to |

Every comparison evaluates to:

```python
True
```

or:

```python
False
```

---

## 23. Comparison Examples

```python
A = 5
B = 3

print(A > B)
```

Output:

```text
True
```

Another example:

```python
A = 5
B = 7

print(A > B)
```

Output:

```text
False
```

---

## 24. Turning Questions into Comparisons

Is X bigger than Y?

```python
X > Y
```

Is Y at least Z?

```python
Y >= Z
```

Are X and Z the same?

```python
X == Z
```

---

## 25. Logical Operators

Python provides:

```python
and
or
not
```

---

## 26. Logical AND

Both conditions must be `True`.

Example:

```python
(year12 == "Yes") and (ielts > 6)
```

The result is `True` only when both conditions are true.

---

## 27. Logical OR

At least one condition must be `True`.

Example:

```python
(farecard == "Yes") or (cash > 2)
```

The result is false only when both conditions are false.

---

## 28. Logical NOT

`not` reverses a Boolean value.

```python
not True
```

Result:

```text
False
```

```python
not False
```

Result:

```text
True
```

---

## 29. Built-in Methods and Libraries

Libraries organise reusable programs and functionality.

A general method call can be represented as:

```text
result = ClassName.method_name(argument1, argument2)
```

Important parts include:

- Class
- Method
- Arguments
- Return value

When calling a method, check:

- Method name
- Return type
- Number of arguments
- Argument types
- Argument order

---

## 30. Python Math Library

Import the library:

```python
import math
```

Square root:

```python
root = math.sqrt(25)
```

Power:

```python
power = math.pow(2, 3)
```

The `math` module provides reusable functions for:

- Square roots
- Powers
- Trigonometry
- Other mathematical calculations

---

## Example Program

```python
import math

name = "VIT"
score = 75
weight = 62.8
height = 168

print(name)
print(score)
print(weight)
print(height)

print(score > 50)

root = math.sqrt(25)
power = math.pow(2, 3)

print(root)
print(power)
```

---

## Quick Reference

| Concept | Example |
|---|---|
| Integer | `10` |
| Float | `10.5` |
| String | `"VIT"` |
| Boolean | `True` |
| Variable | `score = 75` |
| Convert to integer | `int(68.2)` |
| Addition | `x + y` |
| Subtraction | `x - y` |
| Multiplication | `x * y` |
| Division | `x / y` |
| Remainder | `x % y` |
| Equal | `x == y` |
| Not equal | `x != y` |
| Greater than | `x > y` |
| Less than | `x < y` |
| AND | `and` |
| OR | `or` |
| NOT | `not` |
| Math library | `import math` |
| Square root | `math.sqrt(25)` |
| Power | `math.pow(2, 3)` |

---

## Key Takeaways

- Data types give values meaning.
- Variables name and store values.
- Python determines variable types from assigned values.
- Expressions combine operands and operators.
- Mathematical operators perform calculations.
- Comparison operators return `True` or `False`.
- Logical operators combine conditions.
- Operator precedence determines calculation order.
- Libraries provide reusable functionality.
- Python's `math` module provides mathematical functions.
