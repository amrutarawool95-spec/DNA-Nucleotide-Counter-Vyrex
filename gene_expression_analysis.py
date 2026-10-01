"""
Gene Expression Analysis
Finds the top 10 most highly expressed genes in an expression CSV.

Expected CSV format: first column = gene name, other columns = samples.

Install:  pip install pandas matplotlib
Usage:    python gene_expression_analysis.py sample_expression.csv
"""

import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def top_genes(csv_path, n=10):
    df = pd.read_csv(csv_path, index_col=0)
    df["Mean_Expression"] = df.mean(axis=1)
    return df.sort_values("Mean_Expression", ascending=False).head(n)


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "sample_expression.csv"
    top = top_genes(csv_path)

    print("Top 10 expressed genes (mean across samples)\n")
    print(top["Mean_Expression"].round(2).to_string())

    top["Mean_Expression"][::-1].plot(kind="barh", color="teal", figsize=(8, 5))
    plt.xlabel("Mean expression")
    plt.title("Top 10 expressed genes")
    plt.tight_layout()
    plt.savefig("top10_genes.png", dpi=150)
    top.to_csv("top10_genes.csv")
    print("\nSaved: top10_genes.png, top10_genes.csv")


if __name__ == "__main__":
    main()
  
