# Lexical Analyzer

This is a simple program that reads code from a text file and identifies different parts of the code like keywords, identifiers, numbers, etc.

## What it does

- Reads a text file containing code
- Removes comments
- Identifies different types of tokens:
  - Keywords (if, else, while, etc.)
  - Identifiers (variable names)
  - Integers (whole numbers)
  - Floats (decimal numbers)
  - Operators (+, -, *, /, etc.)
  - Separators (parentheses, braces, etc.)
- Prints out the tokens it finds

## How to use it

1. Save the Python file to your computer
2. Create a text file with some code in it
3. Run this command:
   ```
   python lexical_analyzer.py your_code_file.txt
   ```

## Example

If your code file has:
```
if (a >= b)
{
    return 0;
} //this is a comment
```

The output will be:
```
Set of lexemes and tokens (<lexemes> = <tokens>)
"
**"if"** = keyword
**"("** = separator
**"a"** = identifier
**">="** = operator
**"b"** = identifier
**")"** = separator
**"{"** = separator
**"return"** = keyword
**"0"** = integer
**";"** = separator
**"}"** = separator
"
```

## Important notes

- The program ignores comments and whitespace
- The program works with basic C-style syntax
- If there are errors in the code file, some tokens might be marked as "unknown"
