from bz2 import BZ2File
from pathlib import Path


def read_file(path):
    path = Path(path)
    filehandler = BZ2File if path.suffix == ".bz2" else open
    with filehandler(path) as txtfile:
        yield from txtfile.readlines()


def fasta_seqs(lines):
    meta, sequence = None, ""
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if meta:  # finished last seq
                yield meta, sequence
                # reset, we are processing the next seq
                sequence = ""
            meta = line[1:]
        elif meta is not None:
            sequence += line
        else:
            continue
    yield meta, sequence
