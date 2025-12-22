# Example Pipeline

This is a basic example repository.

## Getting Started

Run the script using python:

```bash
python hello.py
```

## Documentation

Documentation is automatically generated from the code docstrings and published to the GitHub Wiki.

To update the documentation:
1. Edit the docstrings in the Python files.
2. Push your changes to the `master` branch.
3. The GitHub Action `Update Wiki Documentation` will run `scripts/generate_wiki.py` and update the Wiki.
