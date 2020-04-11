# JSI - Indented JavaScript Transpiler

> Write JavaScript with Python-like indentation syntax — no more curly braces!

**JSI** (JavaScript Indented) is a transpiler that converts a Python-like indentation-based syntax into standard JavaScript. If you love Python's clean, bracket-free syntax but work with JavaScript, this tool is for you.

---

## Table of Contents

- [What is JSI?](#what-is-jsi)
- [Quick Example](#quick-example)
- [Installation](#installation)
- [Usage](#usage)
- [Syntax Guide](#syntax-guide)
- [Important Notes](#important-notes)
- [Error Handling](#error-handling)
- [Contributing](#contributing)

---

## What is JSI?

JSI introduces an alternative syntax for writing JavaScript code:

| Traditional JS | JSI Syntax |
|----------------|------------|
| Curly braces `{}` | Colons `:` + indentation |
| Verbose block definitions | Clean, Python-like structure |

The transpiler reads `.jsi` files and outputs standard `.js` files that run anywhere JavaScript runs.

---

## Quick Example

**Before (JSI syntax):**
```javascript
function greet(name):
    console.log("Hello, " + name)

const double = (x) => :
    return x * 2
```

**After (JavaScript output):**
```javascript
function greet(name){
    console.log("Hello, " + name)
}

const double = (x) => {
    return x * 2
}
```

---

## Installation

### Prerequisites

- **Python 3.x** installed on your system

### Setup

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/Indented-javascript-transpiler.git
   cd Indented-javascript-transpiler
   ```

2. (Optional) Make the transpiler executable globally:
   ```bash
   chmod +x compiler.py
   ```

No additional dependencies required — the transpiler uses only Python's standard library.

---

## Usage

### Basic Command

```bash
python3 compiler.py <input.jsi> [output.js]
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `input.jsi` | ✓ | Your source file in JSI format |
| `output.js` | ✗ | Output file name (defaults to input name with `.js` extension) |

### Examples

```bash
# Transpile app.jsi → app.js
python3 compiler.py app.jsi

# Transpile with custom output name
python3 compiler.py input.jsi bundle.js

# Transpile files in subdirectories
python3 compiler.py src/main.jsi
```

### Help

Run without arguments to see usage information:

```bash
python3 compiler.py
```

---

## Syntax Guide

### Basic Rules

1. **Replace `{` with `:`** — Use a colon at the end of the line instead of an opening brace
2. **Use indentation** — 4 spaces define the scope (like Python)
3. **No closing braces needed** — The transpiler handles them automatically

### Functions

```javascript
// Classic function
function sayHello():
    console.log("Hello!")

// Arrow function
const add = (a, b) => :
    return a + b
```

### Conditionals

```javascript
if (x > 10) :
    console.log("Greater than 10")
else :
    console.log("10 or less")
```

### Objects

Use `:` for simple objects and `::` for nested objects:

```javascript
const user = :
    name: "John",
    age: 30,
    address ::
        city: "Paris",
        country: "France"
```

**Transpiles to:**
```javascript
const user = {
    name: "John",
    age: 30,
    address :{
        city: "Paris",
        country: "France"
    }
}
```

### Classes

```javascript
class Animal :
    constructor(name):
        this.name = name
    
    speak():
        console.log(this.name + " makes a sound")
```

### Arrow Functions in Callbacks

When using arrow functions inside parentheses (like `.map()`, `.filter()`), place the closing `)` on a new line:

```javascript
const numbers = [1, 2, 3]
const doubled = numbers.map((n) => :
    return n * 2
)
```

---

## Important Notes

> **⚠️ Tab Configuration**  
> Your text editor must use **4 spaces** for indentation (not tabs). This is required for the transpiler to work correctly.

### Syntax Summary

| Pattern | JSI Syntax | Notes |
|---------|------------|-------|
| Open block | `:` at end of line | Replaces `{` |
| Nested object | `::` | For objects inside objects |
| Scope | 4-space indentation | Must be consistent |
| Callback closing | `)` on new line | For arrow functions in parentheses |

---

## Error Handling

The transpiler provides clear error messages:

```bash
$ python compiler.py nonexistent.jsi
Error: File 'nonexistent.jsi' not found.
```

- **Syntax errors** in your JavaScript logic will appear in the generated `.js` file
- For issues specific to the transpiler (not your JS code), please [open an issue](../../issues)

---

## Contributing

This is an **open source project** — contributions are welcome!

- Check the [Issues tab](../../issues) for ways to help
- Feel free to submit pull requests with improvements
- Share your ideas and suggestions

---

## License

This project is open source. See the repository for license details.

---

**Happy coding without curly braces! 🎉**
