#!/usr/bin/env python
"""Count bases in a DNA sequence"""

import argparse

from tutorial.io import read_file, fasta_seqs


def count_bases(fasta_seqitr):
    # could also use collections.defaultdict
    bases = {base: 0 for base in "AGCTN.-"}
    for _, seq in fasta_seqitr:
        for base in seq:
            bases[base.upper()] += 1
    return bases


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("fasta_file", help="Path to fasta file (maybe BZipped)")

if __name__ == "__main__":
    opts = parser.parse_args()
    fasta = read_file(opts.fasta_file)
    seqitr = fasta_seqs(fasta)
    res = count_bases(seqitr)
    print(res)
