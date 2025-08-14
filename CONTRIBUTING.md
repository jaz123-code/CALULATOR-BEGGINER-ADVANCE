# Contributing to Calculator Project

Thank you for your interest in contributing to the Calculator Project! This document provides guidelines for contributing to this educational project.

## Table of Contents
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## Getting Started

This project consists of two main calculators:
1. **Beginner CLI Calculator** (`beginner-cli/`) - A simple command-line calculator for learning Python basics
2. **Advanced GUI Calculator** (`advanced-gui/`) - A sophisticated graphical calculator with advanced features

## Project Structure

```
calculator-project/
├── beginner-cli/          # Simple CLI calculator
├── advanced-gui/          # Advanced GUI calculator  
├── docs/                  # Project documentation
├── examples/              # Usage examples and demos
├── tests/                 # Test suites
└── .github/              # GitHub templates and workflows
```

## Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd calculator-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install development dependencies** (optional)
   ```bash
   pip install pytest black flake8
   ```

## Contributing Guidelines

### Issues
- Check existing issues before creating a new one
- Use the appropriate issue template (Bug Report or Feature Request)
- Provide clear descriptions and reproduction steps
- Label issues appropriately

### Pull Requests
- Fork the repository and create a feature branch
- Follow the pull request template
- Ensure your code follows the project's style guidelines
- Add tests for new functionality
- Update documentation as needed

### Code Organization
- **Beginner CLI Calculator**: Keep code simple and well-commented for educational purposes
- **Advanced GUI Calculator**: More complex features and optimizations are welcome
- Shared utilities should go in appropriate modules

## Code Style

### Python Style Guidelines
- Follow PEP 8 style guidelines
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and small when possible

### Documentation
- Comment complex logic thoroughly
- Update README files when adding new features
- Include examples in docstrings

### Formatting (Optional)
- Use `black` for code formatting: `black .`
- Use `flake8` for linting: `flake8 .`

## Testing

- Write tests for new features and bug fixes
- Run tests before submitting: `pytest tests/`
- Ensure all tests pass
- Include both unit tests and integration tests when appropriate

### Test Structure
```
tests/
├── test_beginner_cli/     # Tests for CLI calculator
├── test_advanced_gui/     # Tests for GUI calculator
└── test_utils/           # Tests for shared utilities
```

## Submitting Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following the guidelines above
   - Add tests for your changes
   - Update documentation

3. **Test your changes**
   ```bash
   pytest tests/
   python -m beginner-cli.calculator_beginner  # Test CLI
   python -m advanced-gui.calculator_advanced   # Test GUI
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Use the pull request template
   - Provide a clear description of your changes
   - Link to any related issues

## History Files

The calculators may generate history files to track calculations. These files should be:
- Ignored in git (already configured in `.gitignore`)
- Stored either in:
  - Project root (ignored via `.gitignore`)
  - User cache directory (`~/.cache/calculator-project/` on Linux/Mac, `%APPDATA%/calculator-project/` on Windows)

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with the question label
- Check existing documentation in the `docs/` directory
- Review similar issues or pull requests

Thank you for contributing to the Calculator Project!
