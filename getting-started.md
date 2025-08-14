# Getting Started with Calculator Project

Welcome to the Calculator Project! This guide will help you set up and start using both calculator implementations.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/calculator-project.git
cd calculator-project
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Quick Start

### Beginner CLI Calculator

The CLI calculator is perfect for learning Python basics:

```bash
python -m beginner-cli.calculator_beginner
```

**Features:**
- Basic arithmetic operations (+, -, ×, ÷)
- Input validation and error handling
- Calculation history
- Simple command-line interface

### Advanced GUI Calculator

The GUI calculator offers advanced mathematical functions:

```bash
python -m advanced-gui.calculator_advanced
```

**Features:**
- All basic arithmetic operations
- Scientific functions (trigonometry, logarithms)
- Memory operations (M+, M-, MR, MC)
- Modern graphical interface
- Keyboard shortcuts
- Export calculation history

## Project Structure Overview

```
calculator-project/
├── beginner-cli/          # Simple CLI calculator
├── advanced-gui/          # Advanced GUI calculator
├── docs/                  # Documentation
├── examples/              # Demo scripts
├── tests/                 # Test suites
└── .github/              # GitHub templates
```

## Next Steps

1. **Run the Examples**: Check out the demo scripts in `examples/`
2. **Read the Documentation**: Explore module-specific docs in each calculator directory
3. **Run Tests**: Execute `pytest tests/` to run the test suite
4. **Contribute**: See `CONTRIBUTING.md` for contribution guidelines

## Getting Help

- 📖 Check the detailed documentation in each module
- 🐛 Report bugs using GitHub issues
- 💡 Request features using GitHub issue templates
- 🤝 See `CONTRIBUTING.md` for how to contribute

## Troubleshooting

### Common Issues

**Import Errors**: Make sure you've installed all dependencies with `pip install -r requirements.txt`

**GUI Not Starting**: Ensure tkinter is installed (usually comes with Python)

**Permission Errors**: Use virtual environment and ensure proper file permissions

**History File Issues**: History files are automatically managed and stored in appropriate locations

Happy calculating! 🧮
