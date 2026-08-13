# Practical Exercise 02 - Data Types, Variables and Operators

> Practice based on the concepts and examples covered in ITAP1001 Lesson 2.

---

## Question 1 - Identify Data Types

### A

```python
534
```

**Answer:** Integer (`int`)

### B

```python
5.49
```

**Answer:** Floating-point (`float`)

### C

```python
"VIT"
```

**Answer:** String (`str`)

### D

```python
True
```

**Answer:** Boolean (`bool`)

### E

```python
88.0
```

**Answer:** Floating-point (`float`)

---

## Question 2 - Valid Variable Names

### `donald`

**Valid**

### `donald_trump`

**Valid**

### `times7`

**Valid**

### `7times`

**Invalid** - variable names cannot begin with a number.

### `here.there`

**Invalid** - periods cannot be used.

### `there+goes`

**Invalid** - `+` cannot be used.

### `for`

**Invalid** - `for` is a Python reserved word.

---

## Question 3 - Variable Assignment

```python
name = "xyz"
weight = 62.8
height = 168
```

Types:

```text
name   → string
weight → float
height → integer
```

---

## Question 4 - Integer Conversion

```python
weight = int(68.2)
print(weight)
```

Output:

```text
68
```

```python
height = int(175.7)
print(height)
```

Output:

```text
175
```

`int()` removes the fractional part rather than rounding it.

---

## Question 5 - Mathematical Expression

Evaluate:

```python
8 * 9
```

Answer:

```text
72
```

---

## Question 6 - Variables in Expressions

```python
y = 9
x = 8 * y
```

`x` becomes:

```text
72
```

Then:

```python
z = x - 13
```

`z` becomes:

```text
59
```

---

## Question 7 - Mathematical Operators

### Addition

```python
10 + 5
```

Answer:

```text
15
```

### Subtraction

```python
10 - 5
```

Answer:

```text
5
```

### Multiplication

```python
10 * 5
```

Answer:

```text
50
```

### Division

```python
5.0 / 2
```

Answer:

```text
2.5
```

---

## Question 8 - Remainder

```python
7 % 3
```

Answer:

```text
1
```

```python
12 % 3
```

Answer:

```text
0
```

---

## Question 9 - Increment

```python
count = 5
count += 1

print(count)
```

Output:

```text
6
```

---

## Question 10 - Decrement

```python
count = 5
count -= 1

print(count)
```

Output:

```text
4
```

---

## Question 11 - Operator Precedence

Evaluate:

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

Answer:

```text
14
```

---

## Question 12 - Parentheses

Evaluate:

```python
(2 + 3) * 4
```

First:

```text
2 + 3 = 5
```

Then:

```text
5 * 4 = 20
```

Answer:

```text
20
```

---

## Question 13 - Comparison Operators

```python
A = 5
B = 3

print(A > B)
```

Output:

```text
True
```

---

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

```python
A = 5
B = 5

print(A > B)
```

Output:

```text
False
```

---

## Question 14 - Translate Questions to Python

Is X bigger than Y?

```python
X > Y
```

Is Y at least Z?

```python
Y >= Z
```

Are X and Z equal?

```python
X == Z
```

---

## Question 15 - Logical AND

```python
year12 = "Yes"
ielts = 7

eligible = (year12 == "Yes") and (ielts > 6)

print(eligible)
```

Output:

```text
True
```

Both conditions are true.

---

## Question 16 - Logical OR

```python
farecard = "No"
cash = 5

can_travel = (farecard == "Yes") or (cash > 2)

print(can_travel)
```

Output:

```text
True
```

Only one condition needs to be true.

---

## Question 17 - Logical NOT

```python
print(not True)
```

Output:

```text
False
```

```python
print(not False)
```

Output:

```text
True
```

---

## Question 18 - Python Math Library

```python
import math

root = math.sqrt(25)

print(root)
```

Output:

```text
5.0
```

---

## Question 19 - Power

```python
import math

power = math.pow(2, 3)

print(power)
```

Output:

```text
8.0
```

---

## Complete Practice Program

```python
import math

# Variables and data types
name = "VIT"
score = 75
weight = 62.8
height = 168

print(name)
print(score)
print(weight)
print(height)

# Integer conversion
converted_weight = int(weight)
print(converted_weight)

# Mathematical operators
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(5.0 / 2)
print(7 % 3)

# Increment and decrement
count = 5
count += 1
print(count)

count -= 1
print(count)

# Comparison operators
print(score > 50)
print(score == 75)
print(score != 100)

# Logical operators
year12 = "Yes"
ielts = 7

eligible = (year12 == "Yes") and (ielts > 6)
print(eligible)

farecard = "No"
cash = 5

can_travel = (farecard == "Yes") or (cash > 2)
print(can_travel)

print(not False)

# Math library
root = math.sqrt(25)
power = math.pow(2, 3)

print(root)
print(power)
```

---

## What I Practised

✅ Data Types  
✅ Variable Naming  
✅ Variable Assignment  
✅ Integer Conversion  
✅ Mathematical Expressions  
✅ Mathematical Operators  
✅ Remainder Operator  
✅ Increment and Decrement  
✅ Operator Precedence  
✅ Comparison Operators  
✅ Logical Operators  
✅ Python Math Library
