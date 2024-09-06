Arithmetic Formatter

This project provides an arithmetic formatter that arranges arithmetic problems vertically and side-by-side, similar to how they are presented in primary school. The arithmetic_arranger function formats a list of arithmetic problems into a clean, readable output with optional results.
Features:

    Vertical Alignment: Arranges problems in a vertical format with numbers and operators aligned correctly.
    Support for Addition and Subtraction: Handles arithmetic problems involving addition and subtraction.
    Error Handling: Validates input for errors such as invalid operators, non-digit characters, and numbers exceeding four digits.
    Optional Results: Can display the results of the arithmetic operations if requested.
    
Error Handling:

    Too Many Problems: Returns an error if more than five problems are provided.
    Invalid Operators: Returns an error if operators other than '+' or '-' are used.
    Non-Digit Characters: Returns an error if numbers contain non-digit characters.
    Excessive Digits: Returns an error if any number exceeds four digits.
