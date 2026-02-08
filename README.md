# Manual Duplex PDF Combiner
A Python CLI tool designed to interleave 2 separate PDF files (front scans and back scans) into a single duplex document.
This is specifically built for users with scanners that does not support automatic duplex scanning.

## Prerequisites
- Python 3.x
- pypdf library
- tqdm library

### Install dependencies via pip
```bash
pip install pypdf tqdm
```

## Usage
- Scan Fronts: Scan all front pages (1, 3, 5, ...) into the first PDF.
- Scan Backs: Flip the stack and scan all back pages (6, 4, 2, ...) into a second PDF.

Run the script:
```bash
python main.py fronts.pdf backs.pdf
```

### Optional Arguments

#### Custom Output Name
By default, the output name is the current timestamp (YYYYMMDD_HHMMSS.pdf).

Use the `-o` flag to specify a output name.
```bash
python main.py fronts.pdf backs.pdf -o combined.pdf
```

## How It Works
- Ascending Fronts: page 1, 3, 5
- Descending Backs: page 6, 4, 2 (once you flip the documents over)

The script reverses the second file and weaves it into the first to produce a perfectly ordered paged 1, 2, 3, 4, 5, 6 document.
