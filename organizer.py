
import argparse
import shutil
from pathlib import Path

TYPES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".ipynb"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Media": {".mp3", ".mp4", ".mkv", ".wav"},
}


def category(ext):
    return next((name for name, extensions in TYPES.items()
                 if ext in extensions), "Other")


def main():
    parser = argparse.ArgumentParser(
        description="Sort a folder by file type"
    )
    parser.add_argument("folder")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files (default is a dry run)",
    )
    args = parser.parse_args()

    root = Path(args.folder).expanduser()
    if not root.is_dir():
        parser.error(f"Folder does not exist: {root}")

    count = 0
    for file in root.iterdir():
        if not file.is_file():
            continue

        dest = root / category(file.suffix.lower())
        if (dest / file.name).exists():
            print(f"SKIP (exists): {file.name}")
            continue

        print(
            f"{'MOVE' if args.apply else 'WOULD MOVE'}: "
            f"{file.name} -> {dest.name}/"
        )
        if args.apply:
            dest.mkdir(exist_ok=True)
            shutil.move(str(file), str(dest / file.name))
        count += 1

    print(f"\n{count} files "
          f"{'moved' if args.apply else 'would be moved'}.")


if __name__ == "__main__":
    main()
