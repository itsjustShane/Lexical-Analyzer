# Lexical Analyzer Implementation Report

## Code Explanation

### Reading the Input File
```python
def analyze_file(file_path):
    # Open and read the file
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
```
This part opens the input file and reads all its content into a string variable called `code`. If the file doesn't exist, it prints an error message and returns an empty list.

### Removing Comments
```python
# Remove comments (both single-line and multi-line)
code = re.sub(r'//.*', '', code)  # Remove single-line comments
code = re.sub(r'/\*[\s\S]*?\*/', '', code)  # Remove multi-line comments
```
Here we use regular expressions to remove comments. The first line removes single-line comments (anything after `//`), and the second line removes multi-line comments (anything between `/*` and `*/`).

### Defining Token Types
```python
# Define token patterns
keywords = ['if', 'else', 'while', 'for', 'return', 'int', 'float', 'void', 'char', 'double', 'main']
separators = ['(', ')', '{', '}', '[', ']', ';', ',', '.']
operators = ['+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '>=', '<=', '==', '!=', '++', '--']
```
This part defines lists of keywords, separators, and operators that our lexical analyzer will recognize.

### Preparing the Code for Tokenization
```python
# First, let's mark all separators and operators in the code
for sep in separators:
    code = code.replace(sep, f" {sep} ")

# Special case for operators with 2 characters
for op in ['>=', '<=', '==', '!=', '++', '--']:
    code = code.replace(op, f" {op} ")
    
# Then handle single character operators
for op in ['+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^']:
    # Skip if already part of a 2-character operator
    if f" {op} " not in code:
        code = code.replace(op, f" {op} ")
```
This code adds spaces around separators and operators to make them easier to identify when we split the code. We handle two-character operators first, then single-character operators.

### Tokenization
```python
# Split the code by whitespace
words = code.split()

# Analyze each word
for word in words:
    if word in keywords:
        tokens.append(("KEYWORD", word))
    elif word in separators:
        tokens.append(("SEPARATOR", word))
    elif word in operators or word in ['>=', '<=']:
        tokens.append(("OPERATOR", word))
    elif re.match(r'^[0-9]+$', word):  # Check if it's an integer
        tokens.append(("INTEGER", word))
    elif re.match(r'^[0-9]+\.[0-9]+$', word):  # Check if it's a float
        tokens.append(("FLOAT", word))
    elif re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', word):  # Check if it's an identifier
        tokens.append(("IDENTIFIER", word))
    elif word.strip():  # If it's not empty after stripping
        # This is a catch-all for anything we didn't handle
        tokens.append(("UNKNOWN", word))
```
Here we split the code into words using spaces as separators. Then we check each word against our defined patterns:
- If it's in our keywords list, it's a keyword
- If it's in our separators list, it's a separator
- If it's in our operators list, it's an operator
- If it matches a number pattern, it's an integer
- If it matches a decimal number pattern, it's a float
- If it matches an identifier pattern (starts with a letter, followed by letters, numbers, or underscores), it's an identifier
- If it doesn't match any of these patterns but isn't empty, we mark it as unknown

### Output Formatting
```python
def print_tokens(tokens):
    """Print tokens in the required format."""
    print("Set of lexemes and tokens (<lexemes> = <tokens>)")
    print("\"")
    for token_type, lexeme in tokens:
        print(f'**"{lexeme}"** = {token_type.lower()}')
    print("\"")
```
This function prints the tokens in the format required by the assignment.

## Complexity Analysis

### Time Complexity
- Reading the file: O(n) where n is the number of characters in the file
- Comment removal: O(n) where n is the number of characters in the file
- Tokenization: O(k * m) where k is the number of tokens and m is the average token length
- Output printing: O(n) where n is the number of tokens

Overall time complexity: O(n) where n is the number of characters in the file.
Note: O(k*m) ~ O(n) 

### Space Complexity
- Storage for code: O(n) where n is the file size
- Storage for tokens: O(n) where n is the number of tokens

Overall space complexity: O(n) where n is the file size.

## References
1. Regular expressions in Python: https://docs.python.org/3/library/re.html
2. Python file handling: https://docs.python.org/3/tutorial/inputoutput.html
