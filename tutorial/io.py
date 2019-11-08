from bz2 import BZ2File
from pathlib import Path


def read_file(path):
    """Read a possibly bzipped text file line by line

    Parameters
    ----------
    path: str, Path
        File path

    Returns
    -------
    Generator[str, None, None]
        Read the file and return one line at a time

    """
    path = Path(path)
    filehandler = BZ2File if path.suffix == ".bz2" else open
    with filehandler(path) as txtfile:
        yield from txtfile


def fasta_seqs(lines):
    """Read one block of sequence at a time

    Parameters
    ----------
    lines: Iterable[str]
        Iterable that returns text in fasta format one line at a time.  This
        can also be a generator or other iterators that read a fasta file or
        stream lazily.

    Returns
    -------
    Tuple[str, str]
        Metadata, and sequence from the fasta file/stream, one at a time.

    """
    meta, sequence = None, ""
    for line in lines:
        line = (line.decode() if isinstance(line, bytes) else line).strip()
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
