"""
FASTA File Parser (Biopython)
Extracts ID, length and GC content for every sequence in a FASTA file.

Install:  pip install biopython
Usage:    python fasta_parser.py sequences.fasta
          python fasta_parser.py sequences.fasta --csv results.csv
"""

import argparse
import csv

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def parse_fasta(path):
    """Return a list of (id, length, gc_percent) for each record."""
    results = []
    for record in SeqIO.parse(path, "fasta"):
        gc = gc_fraction(record.seq) * 100
        results.append((record.id, len(record.seq), round(gc, 2)))
    return results


def main():
    parser = argparse.ArgumentParser(description="Parse a FASTA file.")
    parser.add_argument("fasta", help="Path to the FASTA file")
    parser.add_argument("--csv", help="Optional: save results to a CSV file")
    args = parser.parse_args()

    results = parse_fasta(args.fasta)

    if not results:
        print("No sequences found. Check that the file is in FASTA format.")
        return

    print(f"{'ID':<25}{'Length':>10}{'GC %':>10}")
    print("-" * 45)
    for seq_id, length, gc in results:
        print(f"{seq_id:<25}{length:>10}{gc:>10}")
    print(f"\nTotal sequences: {len(results)}")

    if args.csv:
        with open(args.csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Length", "GC_percent"])
            writer.writerows(results)
        print(f"Saved to {args.csv}")


if __name__ == "__main__":
    main()
  
