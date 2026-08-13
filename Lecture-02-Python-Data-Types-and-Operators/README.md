# Lecture 02 - Python Variables and Data Types

**Course:** ITAP1001  
**Topic:** Python Programming Fundamentals

## Topics Covered

- Variables
- Strings
- Integers
- Assignment operator
- Multiplication operator
- String repetition
- `print()` function
- Understanding Python output

---

## 1. Variables

A variable is used to store a value.

Example:

```python
x = "5"
y = 2
```

Here:

- `x` stores `"5"`
- `y` stores `2`

The `=` symbol is the assignment operator.

---

## 2. Strings

A string is text placed inside quotation marks.

Example:

```python
x = "5"
```

Even though `5` looks like a number, `"5"` is a string because it is inside quotation marks.

Therefore:

```python
"5"
```

is different from:

```python
5
```

---

## 3. Integers

An integer is a whole number without quotation marks.

Example:

```python
y = 2
```

Here, `2` is an integer.

---

## 4. String vs Integer

Python treats strings and integers differently.

For example:

```python
5 * 2
```

Result:

```text
10
```

But:

```python
"5" * 2
```

Result:

```text
55
```

This happens because `"5"` is a string.

---

## 5. Multiplication Operator

The multiplication operator in Python is:

```text
*
```

With numbers, it performs normal multiplication.

Example:

```python
print(5 * 2)
```

Output:

```text
10
```

---

## 6. String Repetition

When a string is multiplied by an integer, Python repeats the string.

Example:

```python
print("5" * 2)
```

Output:

```text
55
```

Another example:

```python
print("Hello" * 3)
```

Output:

```text
HelloHelloHello
```

---

## 7. Lesson Example

The code practised in this lesson was:

```python
x = "5"

y = 2

print(x * y)
```

### Step 1

```python
x = "5"
```

`x` contains the string `"5"`.

### Step 2

```python
y = 2
```

`y` contains the integer `2`.

### Step 3

Python evaluates:

```python
x * y
```

which becomes:

```python
"5" * 2
```

Because `"5"` is a string, Python repeats it twice.

Result:

```text
55
```

### Step 4

```python
print(x * y)
```

displays:

```text
55
```

---

## 8. print() Function

The `print()` function displays output.

Example:

```python
print("Hello")
```

Output:

```text
Hello
```

It can also print the result of an expression:

```python
print("5" * 2)
```

Output:

```text
55
```

---

## Quick Reference

| Code | Meaning |
|---|---|
| `x = "5"` | Store string `"5"` |
| `y = 2` | Store integer `2` |
| `"5"` | String |
| `5` | Integer |
| `=` | Assignment |
| `*` | Multiplication / repetition |
| `print()` | Display output |
| `"5" * 2` | `55` |
| `5 * 2` | `10` |

---

## Key Takeaway

Data types matter in Python.

```python
5 * 2
```

produces:

```text
10
```

while:

```python
"5" * 2
```

produces:

```text
55
```

because `"5"` is a string rather than an integer.

## Learning Progress

✅ Variables  
✅ Strings  
✅ Integers  
✅ Assignment operator  
✅ Multiplication operator  
✅ String repetition  
✅ Python output

print(x * y)
