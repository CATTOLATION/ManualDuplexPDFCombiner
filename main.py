import os
import sys
import argparse
from datetime import datetime
from pypdf import PdfReader, PdfWriter
from tqdm import tqdm

def combine_duplex(front_path, back_path, output_path=None):
    print("\n" + "="*40)
    print("      PDF DUPLEX MERGE UTILITY")
    print("="*40)

    if not os.path.exists(front_path):
        print(f"[-] ERROR: File '{front_path}' not found.", flush=True)
        sys.exit(1)

    if not os.path.exists(back_path):
        print(f"[-] ERROR: File '{back_path}' not found.", flush=True)
        sys.exit(1)

    if not output_path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"{timestamp}.pdf"

    try:
        front_reader = PdfReader(front_path)
        back_reader = PdfReader(back_path)
        writer = PdfWriter()

        front_pages = front_reader.pages
        back_pages = back_reader.pages

        num_fronts = len(front_pages)
        num_backs = len(back_pages)
        max_range = max(num_fronts, num_backs)

        print(f"[*] Input:  {num_fronts} front pages")
        print(f"[*] Input:  {num_backs} back pages")
        print(f"[*] Target: {output_path}")
        print("-" * 40, flush=True)

        pbar = tqdm(
            range(max_range),
            desc="[+] Processing",
            unit="pair",
            bar_format="{desc}: {percentage:3.0f}% |{bar:20}| {n_fmt}/{total_fmt} [{elapsed}]",
            leave=True
        )

        for i in pbar:
            if i < num_fronts:
                writer.add_page(front_pages[i])

            back_idx = num_backs - 1 - i
            if back_idx >= 0:
                writer.add_page(back_pages[back_idx])

        with open(output_path, "wb") as f:
            writer.write(f)

        print("-" * 40, flush=True)
        print(f"[!] SUCCESS: File generated.")
        print(f"[!] FILENAME: {output_path}")
        print("="*40 + "\n", flush=True)

    except Exception:
        print("\n[-] ERROR: An issue occurred during PDF processing.", flush=True)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interleave front and back PDF scans.")
    parser.add_argument("fronts", help="Front pages PDF")
    parser.add_argument("backs", help="Back pages PDF")
    parser.add_argument("-o", "--output", help="Optional: output name")

    args = parser.parse_args()
    combine_duplex(args.fronts, args.backs, args.output)