#!/usr/bin/env python3
"""
JSI Transpiler - Convert indentation-based JavaScript to standard JavaScript.

Usage:
    python compiler.py <input.jsi> [output.js]

Arguments:
    input.jsi   - Source file in JSI format (required)
    output.js   - Output JavaScript file (optional, defaults to input name with .js extension)
"""

import re
import sys
import os


def transpile(source_code):
    """Transpile JSI code to JavaScript."""
    lines = source_code.splitlines(keepends=True)
    
    # Stack of indentations for closing braces
    stack = []
    result = ""

    for line in lines:
        # Test if closing braces are needed before proceeding
        while len(stack) > 0 and (len(re.findall(" {4}", line)) < len(stack)):
            result += "\t" * (len(stack) - 1) + stack.pop() + "\n"
        
        # Check if line ends with a colon (scope opener)
        if re.match(".*:\n", line) or re.match(".*:$", line):
            line = re.sub(":(\n?)$", "{\\1", line)
            result += line
            stack.append("}")
        else:
            result += line

    # Close any remaining scopes
    while len(stack) > 0:
        result += "\n" + "\t" * (len(stack) - 1) + stack.pop()

    return result


def main():
    # Check arguments
    if len(sys.argv) < 2:
        print("JSI Transpiler - Convert indentation-based JavaScript to standard JavaScript")
        print("")
        print("Usage:")
        print("  python compiler.py <input.jsi> [output.js]")
        print("")
        print("Arguments:")
        print("  input.jsi   - Source file in JSI format (required)")
        print("  output.js   - Output JavaScript file (optional)")
        print("")
        print("Examples:")
        print("  python compiler.py app.jsi              # Creates app.js")
        print("  python compiler.py src/main.jsi         # Creates src/main.js")
        print("  python compiler.py input.jsi output.js  # Custom output name")
        sys.exit(1)

    input_file = sys.argv[1]
    
    # Determine output file name
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Replace .jsi extension with .js, or append .js if no extension
        base_name = os.path.splitext(input_file)[0]
        output_file = base_name + ".js"

    # Read source file
    try:
        with open(input_file, "r") as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except IOError as e:
        print(f"Error: Could not read file '{input_file}': {e}")
        sys.exit(1)

    # Transpile
    result = transpile(source_code)

    # Write output file
    try:
        with open(output_file, "w") as f:
            f.write(result)
    except IOError as e:
        print(f"Error: Could not write to file '{output_file}': {e}")
        sys.exit(1)

    print(f"✓ Transpiled '{input_file}' → '{output_file}'")


if __name__ == "__main__":
    main()
