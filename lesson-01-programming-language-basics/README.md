# Lesson 1: Introduction to Programming Languages

## Lesson Overview

This lesson introduced the fundamental ideas behind software
development and programming languages.

It covered hardware and software, operating systems, programming
language levels, language translators, object-oriented programming,
program-development methods, Visual Studio Code and basic Python
program structure.

## Hardware and Software

### Hardware

Hardware refers to the physical components used in or with a
computer.

Examples include:

- Processor
- Memory
- Storage devices
- Keyboard
- Mouse
- Monitor
- Network adapter

### Software

Software is a collection of code and instructions that tells computer
hardware what tasks to perform.

Examples include:

- Operating systems
- Applications
- Programming tools
- Device drivers
- Utility programs

Hardware performs the physical work, while software provides the
instructions.

## Operating-System Functions

The operating system connects applications to computer hardware and
manages shared resources.

Important operating-system responsibilities include:

- Booting the computer
- Managing memory
- Managing processes
- Managing files and disks
- Controlling devices
- Providing security
- Managing printing
- Providing a user interface

A simplified relationship is:

```text
Applications → Operating System → Hardware
```

## Levels of Programming Languages

### Machine Language

Machine language consists of binary instructions that can be executed
directly by a processor.

It is:

- Fast for the processor to execute
- Difficult for people to read
- Difficult to maintain
- Dependent on a particular processor architecture

### Assembly Language

Assembly language uses short symbolic instructions called mnemonics.

It is more readable than binary machine language, but an assembler
must translate it into machine language before the processor can
execute it.

### High-Level Languages

High-level languages allow programmers to express complex operations
using clearer and more human-readable instructions.

Advantages include:

- Faster development
- Clearer program logic
- Easier maintenance
- Reusable solutions
- Greater portability

Examples include:

- Python
- Java
- C
- C++
- C#
- JavaScript
- Ruby
- PHP

## Language Translators

A language translator converts source code into machine code or an
intermediate form.

### Assembler

An assembler converts assembly-language instructions into machine
language.

### Compiler

A compiler normally translates the whole program before execution.

A compiler:

- Translates the entire source program
- Produces object code or an executable
- Requires recompilation after source-code changes
- Usually produces programs that run quickly

### Interpreter

An interpreter translates and executes instructions step by step.

An interpreter:

- Executes the program one section at a time
- Is useful for testing and debugging
- Does not normally require a separate executable
- May be slower while the program is running

## Object-Oriented Programming

Object-oriented programming structures software around objects that
combine data and behaviour.

### Encapsulation

Encapsulation combines data and related methods inside a class while
protecting its internal details.

### Inheritance

Inheritance allows a new class to reuse or extend features from an
existing class.

### Polymorphism

Polymorphism allows one interface or method name to behave in
different ways.

These principles support modular, reusable and maintainable software.

## Examples of High-Level Languages

### C

C is a procedural language that provides direct control over memory
and system resources.

### C++

C++ builds upon C and adds features such as:

- Classes
- Objects
- Templates
- Object-oriented programming
- Generic programming

C and C++ source code is compiled into object code. A linker then
combines the object code with the required libraries.

### Java

Java source code is compiled into bytecode.

The Java Virtual Machine executes the bytecode on a compatible
platform.

Java supports:

- Object-oriented programming
- Strong typing
- Runtime checking
- Platform portability

### Python

Python is a high-level, interpreted and object-oriented programming
language.

Python is:

- Readable
- Reusable
- Versatile
- Cross-platform
- Suitable for many types of applications

Python programs can be separated into reusable functions and modules
instead of being written as one long sequence of instructions.

## Program-Development Process

Program development should begin by defining the problem before
writing code.

### Problem Analysis

The programmer should identify:

1. **Objective:** What must the program accomplish?
2. **Inputs:** What data will the program receive?
3. **Outputs:** What results must it produce?
4. **Operations:** What processing connects the inputs to the outputs?

### Program Design

A solution may be represented using:

- Algorithms
- Modules
- Pseudocode
- Flowcharts
- Decision tables

A well-designed program is easier to code, test, document and
maintain.

## Algorithm

An algorithm is a clear, finite and ordered series of steps used to
solve a problem.

Example algorithm for adding two numbers:

1. Start
2. Declare two numbers and a result
3. Read the two numbers
4. Add the numbers
5. Display the result
6. Stop

## Pseudocode

Pseudocode describes program logic using structured, human-readable
language without requiring exact programming syntax.

Example:

```text
START
    INPUT first_number
    INPUT second_number
    total = first_number + second_number
    DISPLAY total
STOP
```

## Flowcharts

A flowchart visually represents program steps and control flow.

Common symbols include:

- Oval or rounded rectangle: start or end
- Rectangle: process
- Parallelogram: input or output
- Diamond: decision
- Arrow: flow direction
- Circle: connector

A readable flowchart should:

- Follow a clear direction
- Present steps in logical order
- Avoid unnecessary crossing lines
- Use separate branches for decision outcomes
- Keep labels brief
- Have a clear exit from each process
- Be tested with sample data

### Benefits of Flowcharts

- Improve communication
- Support program analysis
- Document program logic
- Guide coding
- Help with debugging
- Support future maintenance

### Limitations of Flowcharts

- Complex logic can become cluttered
- Changes may require the diagram to be redrawn
- Too much technical detail may hide the main idea

## Decision Tables

A decision table represents conditions and their corresponding
actions in a compact format.

The lesson demonstrated quantity-based discounts:

| Quantity | Discount |
|---|---:|
| Less than 10 | 5% |
| 10 to 49 | 10% |
| 50 to 99 | 15% |
| 100 or more | 20% |

For example, a quantity of 75 receives a 15% discount.

## Coding and Testing Cycle

Programming is an iterative process:

1. Create the program
2. Save the file
3. Run the program
4. Review errors, warnings and results
5. Correct the program
6. Repeat until the expected result is produced

Testing should check:

- Syntax errors
- Runtime errors
- Logic errors
- Normal inputs
- Boundary values
- Unexpected inputs
- Expected outputs

Documentation should begin early and be updated as the program
changes.

## Visual Studio Code

Visual Studio Code is a lightweight and customisable code editor.

It provides:

- Support for multiple programming languages
- Code completion
- Debugging tools
- Breakpoints
- Variable inspection
- Git integration
- Extensions
- Custom themes and settings
- Cross-platform support

## Setting Up Python in Visual Studio Code

The basic setup process is:

1. Install Python.
2. Install Visual Studio Code.
3. Install the Microsoft Python extension.
4. Open or create a project folder.
5. Select the Python interpreter.
6. Create a file ending in `.py`.
7. Use **Run Python File in Terminal**.
8. Configure debugging when required.

## Basic Python Program Structure

A simple Python file may contain:

- A docstring explaining its purpose
- Comments that provide context
- Functions
- An entry point
- Executable statements
- Output using `print()`

Example:

```python
"""Display a welcome message."""


def main():
    """Run the program."""
    print("Welcome to Software Development Fundamentals")


if __name__ == "__main__":
    main()
```

## Types of Programming Errors

### Syntax Error

A syntax error occurs when code does not follow the rules of the
programming language.

Example:

```python
print("Hello"
```

### Runtime Error

A runtime error occurs while the program is executing.

An example is attempting to convert invalid text into a number.

### Logic Error

A logic error occurs when the program runs but produces an incorrect
result because its instructions or conditions are wrong.

## Practical Activity

For this lesson, I designed and implemented a quantity-based discount
calculator in Python.

The practical work contains:

- Problem definition
- Inputs, outputs and operations
- Algorithm
- Pseudocode
- Decision table
- Flowchart
- Python source code
- Input validation
- Sample test cases

## Skills Demonstrated

- Programming-language fundamentals
- Problem analysis
- Algorithms
- Pseudocode
- Flowchart interpretation
- Decision tables
- Conditional logic
- Functions
- Python
- Visual Studio Code
- Testing and documentation
- GitHub repository organisation

## Reflection

This lesson helped me understand that programming should not begin
with code immediately.

A programmer should first understand the problem, identify the input
and output, design the solution and then implement and test it.

I also learned how high-level code is translated for the computer,
how Python programs are executed and how Visual Studio Code supports
writing, running and debugging software.

## Next Steps

- Run the Python discount calculator
- Test it with different quantities
- Add a screenshot of the program output
- Practise identifying syntax, runtime and logic errors
- Continue documenting future lessons
