import re
import sys

def analyze_file(file_path):
    # Open and read the file
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    
    # Remove comments (both single-line and multi-line)
    code = re.sub(r'//.*', '', code)  # Remove single-line comments
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)  # Remove multi-line comments
    
    # Define token patterns
    keywords = ['if', 'else', 'while', 'for', 'return', 'int', 'float', 'void', 'char', 'double', 'main']
    separators = ['(', ')', '{', '}', '[', ']', ';', ',', '.']
    operators = ['+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '>=', '<=', '==', '!=', '++', '--']
    
    # Tokenize the code
    tokens = []
    
    # Split the code into words and symbols
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
    
    return tokens

def print_tokens(tokens):
    """Print tokens in the required format."""
    print("Set of lexemes and tokens (<lexemes> = <tokens>)")
    print("\"")
    for token_type, lexeme in tokens:
        print(f'**"{lexeme}"** = {token_type.lower()}')
    print("\"")

def main():
    # Check if a file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python lexical_analyzer.py <input_file.txt>")
        return
    
    file_path = sys.argv[1]
    tokens = analyze_file(file_path)
    
    if tokens:
        print_tokens(tokens)

if __name__ == "__main__":
    main()
