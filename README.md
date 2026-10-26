# File Organizer

A Python CLI tool that organizes files into folders based on their file extensions.

## Features
- Categorizes images, documents, code, archives, and media
- Dry-run mode by default to preview changes safely
- Skips files if a destination file with the same name already exists

## Usage

Preview file moves:

```bash
python organizer.py F:\Projects\organizer-test
```

Actually move files:

```bash
python organizer.py F:\Projects\organizer-test --apply
```

## Requirements
- Python 3
- No external dependencies