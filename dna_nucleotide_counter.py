"""
DNA Nucleotide Counter
Counts A, T, G and C in a DNA sequence.

Usage:
    python dna_nucleotide_counter.py
    python dna_nucleotide_counter.py ATGCGTACGTTAGC
"""

import sys


def count_nucleotides(sequence):
    """Return a dict with counts of A, T, G, C in the sequence."""
    sequence = sequence.upper().replace(" ", "").replace("\n", "")

    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    invalid = 0

    for base in sequence:
        if base in counts:
            counts[base] += 1
        else:
            invalid += 1

    return counts, invalid, len(sequence)


def main():
    # Take the sequence from the command line, or ask for it
    if len(sys.argv) > 1:
        sequence = sys.argv[1]
    else:
        sequence = input("Enter a DNA sequence: ")

    if not sequence.strip():
        print("No sequence entered.")
        return

    counts, invalid, total = count_nucleotides(sequence)

    print("\nNucleotide counts")
    print("-" * 22)
    for base, n in counts.items():
        percent = (n / total * 100) if total else 0
        print(f"{base}: {n:<6} ({percent:.1f}%)")

    print("-" * 22)
    print(f"Total length: {total}")

    gc = counts["G"] + counts["C"]
    print(f"GC content: {gc / total * 100:.1f}%")

    if invalid:
        print(f"Warning: {invalid} invalid character(s) found (not A, T, G or C).")


if __name__ == "__main__":
    main()
  
