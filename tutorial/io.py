from bz2 import BZ2File
from pathlib import Path


def read_file(path):
    path = Path(path)
    filehandler = BZ2File if path.suffix == ".bz2" else open
    with filehandler(path) as txtfile:
        yield from txtfile.readlines()


def next_fasta_seq(lines):
    meta, sequence = None, ""
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            meta = line
            print(meta)
        elif meta is not None:
            sequence += line
            print(line)
        else:
            continue
    return meta, sequence
