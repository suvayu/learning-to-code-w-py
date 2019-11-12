#!/usr/bin/env python

import sys

from tutorial.io import read_file, fasta_seqs


def count_bases(fasta_seqitr):
    bases = {base: 0 for base in "AGCT"}
    for _, seq in fasta_seqitr:
        for base in seq:
            bases[base] += 1
    return bases


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Expected a fasta file as argument")
    fasta = read_file(sys.argv[1])
    seqitr = fasta_seqs(fasta)
    res = count_bases(seqitr)
    print(res)
