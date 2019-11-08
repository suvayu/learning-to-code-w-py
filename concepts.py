# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   rise:
#     enable_chalkboard: true
#     autolaunch: true
# ---

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # ![Python logo](data/python.ico) Hello Python!

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Python: history and now
#
# - Created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) in 1990.  At the time he was a postdoc at CWI, Amsterdam, currently he is at Dropbox.
# - Named after [**Monty Python**](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus), Guido is a big fan.
# - Development guided by the Python Steering Council,
#   - entirely community led effort,
#   - supported by the Python Software Foundation.

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## The Python ecosystem
#
# - Ease of use among its primary considerations
# - Highly extendable, including through extensions written in lower level languages like C/C++.
# - Natively there are certain performance limitations (e.g. *Global Interpreter Lock* or GIL), but effectively not a limitation as it can be worked around with extensions; e.g. `numpy`, `xarray`, `pandas`, `numba`, `pyarrow`, etc.
# - Writing *native* extensions is easier with `Cython` (Python + `type` information + ability to by-pass the GIL)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Understanding variables
#
# Variables hold a *reference* to a value,
# - can be *objects* of simple *types* (e.g. numbers, strings, booleans),
#
# - user defined types,
#
# - *sequences* or *containers* (contains other variables), and others (esp. in Python).

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Literals
# -

# values
1, 3.14, 0b10, 0x1e, "string", b"bytes"

# + {"slideshow": {"slide_type": "fragment"}}
a = 2.14  # variable assignment: hold a reference to a value
a + 1  # the variable refers to the value later

# + {"slideshow": {"slide_type": "fragment"}}
a # what is a?

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# To refer to an `object` later, you must store a reference to it in a variable

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Numbers

# + {"slideshow": {"slide_type": "-"}}
x, y = 3, 3.0
x, type(x), y, type(y)

# + {"slideshow": {"slide_type": "fragment"}}
# alternate notations for readability
p, q = 10_000, 1.1e4
p, type(p), q, type(q)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Numeric operations

# + {"slideshow": {"slide_type": "-"}}
# increment, similar for most other operators: -=, *=, /=
a = 40
a = a + 1
a += 1
a

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Numeric operations
# -

# division
1 / 2, 4 / 3, 4 / 2

# + {"slideshow": {"slide_type": "fragment"}}
# floor division
1 // 2, 4 // 3, 4 // 2

# + {"slideshow": {"slide_type": "fragment"}}
# modulo/remainder, exponent
4 % 3, 3 ** 3

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Booleans

# + {"slideshow": {"slide_type": "-"}}
eq = p == 10_000
eq, type(eq)

# + {"slideshow": {"slide_type": "fragment"}}
# numbers and strings: 0, empty string, None -> False, everything else -> True
bool(1), bool(0), bool(""), bool("foo"), bool(None)

# + {"slideshow": {"slide_type": "fragment"}}
# containers: empty -> False, has element -> True
bool(list()), bool([1]), bool(set()), bool({1}), bool(dict()), bool({1: 4})

# + {"slideshow": {"slide_type": "subslide"}}
bool(None), bool([]), bool([1])
# -

bool([None])  # given the above, what does this evaluate to?

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Boolean operations
# -

-2 > 3 or -1 < 0, 2 > 3 and -1 > 3, not True

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# ##### Truth table
#
# <table>
# <tr><th>Logical OR</th><th>Logical AND</th></tr>
# <tr><td>
#
# | `or` | T | F |
# |:----:|---|---|
# | T    | T | T |
# | F    | T | F |
#
# </td><td>
#
# | `and` | T | F |
# |:-----:|---|---|
# | T     | T | F |
# | F     | F | F |
#
# </td></tr> </table>

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Strings

# + {"slideshow": {"slide_type": "-"}}
txt = "foo bar baz"  # 'also valid'
txt, type(txt)

# + {"slideshow": {"slide_type": "fragment"}}
# escaping, and nested quotes
'Don\'t be an ass', "Don't be an ass"

# + {"slideshow": {"slide_type": "subslide"}}
multi = "First\nSecond"
multi

# + {"slideshow": {"slide_type": "fragment"}}
print(multi)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Triple quoted strings
# -

prose = """This is a pre-formatted string.

You may have paragraphs, and lists:
- an item
- no need for "escaping"

    Or whatever you like

"""
print(prose)
prose

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### String operations

# + {"slideshow": {"slide_type": "-"}}
# concatenation
"foo" "bar"

# + {"slideshow": {"slide_type": "fragment"}}
"foo"\
"bar"

# + {"slideshow": {"slide_type": "fragment"}}
# append
a = "foo"
b = "bar"
a + b

# + {"slideshow": {"slide_type": "subslide"}}
# multiply
"--8<-" * 5

# + {"slideshow": {"slide_type": "fragment"}}
# in
"foo" in "foo bar baz", "foo" not in "foo bar baz"


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### User defined types

# + {"slideshow": {"slide_type": "-"}}
class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass("{self.name}")'


instance = MyClass("foo")

instance, type(instance)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Containers

# + {"slideshow": {"slide_type": "-"}}
l = [1, 2.0, 3, 4.0, "foo", True]
t1 = (1, 3.14, True)

type(l), type(t1)

# + {"slideshow": {"slide_type": "subslide"}}
# append
l + [1, 2]

# + {"slideshow": {"slide_type": "fragment"}}
# multiply
t1 * 3

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Indexing
#
# Syntax: `container[index]`

# + {"slideshow": {"slide_type": "-"}}
l[0] == t1[0] == 1

# + {"slideshow": {"slide_type": "fragment"}}
l[-1] == True

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Slicing
#
# Syntax: `container[start:stop:step]` (only one is required)
# -

l, l[:2], l[1:3]

# + {"slideshow": {"slide_type": "fragment"}}
l[0:4:2], l[::3]

# + {"slideshow": {"slide_type": "fragment"}}
txt = "foo bar baz"
txt[4:7]

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Mutable and immutable types
#
# Certain types, once created cannot be "edited"; e.g. `str`, `tuple`.

# + {"slideshow": {"slide_type": "fragment"}}
l  # mutable

# + {"slideshow": {"slide_type": "-"}}
l[0] = 1000
l

# + {"slideshow": {"slide_type": "subslide"}}
t1, txt  # immutable

# + {"slideshow": {"slide_type": "fragment"}}
t1[0] = 1000

# + {"slideshow": {"slide_type": "fragment"}}
txt[5] = "e"

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Operators & type conversion
#
# - Implicit type conversion on supported operations
# - Result is the most representative type: support both operands **and** the result
# -

1 +  3.14, type(1 + 3.14), 1 + True, type(1 + True), 2.16 * False

# + {"slideshow": {"slide_type": "subslide"}}
"1" + 1
# -

1 + "1"  # same for: "foo" - "foo"

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Flow control
#
# - conditionals
# - iteration
# - callable / functions: reusable routines

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Conditionals
# -

# if .. else ..
txt = "foo bar baz"
if "foo" in txt:
    pass
elif "bar" in txt:  # optional
    pass
else:  # optional
    pass

# + {"slideshow": {"slide_type": "fragment"}}
# ternary conditional
par = None
5 if par is None else par

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Iteration
#
# #### `for` loops
# -

# iterate over items
t1 = (1, 3.14, True)
for i in t1:
    print(i)

# + {"slideshow": {"slide_type": "subslide"}}
# iterate by index
for i in range(len(t1)):  # len(..) returns the length of a sequence
    print(t1[i])

# + {"slideshow": {"slide_type": "fragment"}}
# iterate by index
for i in range(1, 10, 2):
    print(i)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### `while` loops
#
# *What does the following do?*
# -

# flexible iteration
txt = "foo bar baz"
i = 0
res = []
while i < len(txt):
    res += [txt[-1 - i]]
    i += 1
"".join(res)  # calling: str.join(Iterable[str]) -> str

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# **Ans:** *Reverse the string `txt`*

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### `break` and `continue` statements
#
# *What does the following do?*

# + {"slideshow": {"slide_type": "-"}}
txt = "foo bar baz"
i = 0
while i < len(txt):
    if txt[i] == "b":
        break  # prematurely ends any iteration
    i += 1
txt[:i]

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# **Ans:** *Finds the first b / Shows the string upto the first b*

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# *What does the following do?*
# -

txt = "foo bar baz"
i = 0
res = ""
while i < len(txt):
    char = txt[i]
    i += 1
    if char == "b":
        continue  # skip this iteration
    res += char
res


# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# **Ans:** *Remove all b-s from the string*

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Callables / Functions
#
# - Wraps a code block that can be reused, arguments act as parameters
# - Ends in a `return` statement; returns control back to the caller

# +
def add(i, j):
    return i + j

def sub(i, j):
    return i - j

def op(i, j, operator=add):  # default operator: addition
    """Applies a binary operator to two numbers"""  # <- docstring
    return operator(i, j)


# + {"slideshow": {"slide_type": "subslide"}}
op(3, 4)  # addition

# + {"slideshow": {"slide_type": "fragment"}}
op(3, 4, sub)  # subtraction

# + {"slideshow": {"slide_type": "fragment"}}
# multiply w/ anonymous function
op(3, 4, lambda i, j: i * j)


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# In the absence of a `return` statement, `return None`
# -

def myfunc():
    pass


# + {"slideshow": {"slide_type": "fragment"}}
res = myfunc()
print(res)

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# #### Anonymous / `lambda` functions
#
# - no statements
# - only expressions

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Positional and keyword arguments
# -


def myfunc(pos1, pos2, kw1="foo", kw2="bar"):
    print(pos1, pos2, kw1, kw2)


# + {"slideshow": {"slide_type": "fragment"}}
# what's the print order?
myfunc(1, 2, 3, 4)
# -

myfunc(1, 2, kw2="random", kw1="order")

myfunc(5, kw1="bla", pos2=99, kw2="dibla")

# + {"slideshow": {"slide_type": "subslide"}}
# explain the errors
myfunc()
# -

myfunc(42)

myfunc(kw1=42)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Variable scope
# -

# Code blocks, at any indentation level, are in the *same scope*


# +
num = 42

for i in range(3):
    if i == 0:
        assert num == 42
        num = 5
    assert num == 5

assert num == 5
# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Functions have access to variables in the current scope *during execution*


# +
num = 42

def testfn1():
    assert num == 42, f"{num} is not 42"
# + {"slideshow": {"slide_type": "fragment"}}
testfn1()
# + {"slideshow": {"slide_type": "fragment"}}
num = 5
testfn1()
# + {"slideshow": {"slide_type": "subslide"}}
del num
# -

testfn1()

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# When 2 variables have the same name, the variable in the inner most scope is said to *shadow* the outer variable

# +
num = 42

def testfn2():
    num = 5
    assert num == 5, f"{num} is not 5"


# -


testfn2()


# + {"slideshow": {"slide_type": "subslide"}}
assert num == 5, f"{num} is not 5"

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# *Review errors at this point*

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# <center><strong>&#9646;&#9646;</strong></center>

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### How to help yourself
#
# - Use `help(object|"syntax token")`
# - docstrings
# - function signatures
# - Library reference, tutorials, HOWTOs, etc @ [Python.org](https://docs.python.org/3.7/)
# -



# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Problem 1
#
# - Read a sequence, and count the number of bases of each type.
# - Print out the counts as a table, or write it to a CSV file.

# +
from tutorial.io import read_file, fasta_seqs

# `next` will work only twice, as the file has only two sequences
fasta = read_file("data/example.fa")
seq_itr = fasta_seqs(fasta)
_, seq1 = next(seq_itr)  # work with seq1, it's a string
# -

seq1[:12]

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Problem 2
#
# - Read a sequence, and identify the sequence of *Codons*.
# - Print out the position and codon as a table, or write it to a CSV file.

# +
from tutorial.seq import CODON_MAP

_, seq2 = next(seq_itr)
# CODON_MAP["START"], list of starting seq
# CODON_MAP["STOP"], list of all stopping seqs
# CODON_MAP["REST"], list of all other seqs
# -

CODON_MAP["STOP"]

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# <center><strong>&#9654;</strong></center>

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # ![Python logo](data/python.ico) More Python concepts

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Format strings
# -

fmt_float = "{0} {0:.3f} {0:+.3f} {0: .3f} {0:.3e} {0:.3g}"

# + {"slideshow": {"slide_type": "fragment"}}
fmt_float.format(79 / 3)
# -

fmt_float.format(-79 / 3)

# + {"slideshow": {"slide_type": "subslide"}}
fmt = "{} {} {}"
# -

fmt.format("foo", "bar", "baz")

# + {"slideshow": {"slide_type": "fragment"}}
fmt = "{a} {b} {c}"
# -

fmt.format(a="foo", c="bar", b="baz")

# + {"slideshow": {"slide_type": "subslide"}}
a, b, c = "foo bar baz".split()  # calling: str.split() -> List[str]
f"{a} {b} {c} {c.upper()}"

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Function calls
#
# ### Argument unpacking
# -


def myfunc(pos1, pos2, kw1="foo", kw2="bar"):
    print(pos1, pos2, kw1, kw2)


x, y, z = (1, 2, 3)
x, y, z

# + {"slideshow": {"slide_type": "subslide"}}
t1 = (1, 2, "foo", "bar")
myfunc(*t1)  # also works for lists

# + {"slideshow": {"slide_type": "fragment"}}
d1 = {"kw1": "foo", "kw2": "bar"}
myfunc(*t1[:2], **d1)


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Arbitrary arguments
#
# - positional arguments, followed by keyword arguments
# -

def myflexiblefn(pos1, *args, kw1="foo", **kwargs):
    print(pos1, kw1, args, kwargs)


myflexiblefn(1, 2, 3, kw1="foo", kw2="bar", kw3="baz")

# argument order: positional, *args, keyword, **kwargs
myflexiblefn(**d1, *t1[:2])

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# **Note:** default arguments should never be mutable objects, e.g. empty containers


# +
def fn1(a, b=42):  # a-okay!
    pass

def fn1(a, b=[]):  # not okay!
    pass

def fn1(a, b=None):
    # use this idiom instead
    if b is None:
        b = []
    pass


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Containers & Iteration
#
# ### List comprehension
# -

[i for i in range(5)]

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# #### with conditionals
# -

[i for i in range(10) if i % 2]

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Sets
#
# - elements are unique
# -

set("foo bar baz")

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# #### Set comprehension
# -

{c for c in "foo bar baz"}

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Operations with `set`s
# -

a_, b_, c_ = set("foo"), set("bar"), set("baz")

b_.intersection(c_), a_.isdisjoint(b_)

b_.difference(c_), c_.difference(b_)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Dictionaries
# -

week = {
    "mon": 9,
    "tues": 1,
    "wed": 2,
    "thurs": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
}
week

week["mon"] = 0
week

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Dictionary comprehension

# + {"slideshow": {"slide_type": "-"}}
{k: (v, v < 5) for k, v in week.items()}  # add weekday boolean flag

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Merging tuples, lists, and dictionaries
# -

t1 = (1, 2)
t2 = ("foo", "bar", "baz")
(42, *t1, *t2)  # same for lists

# + {"slideshow": {"slide_type": "fragment"}}
d0 = {"a": 1, "b": 2}
d1 = {"c": 3, "d": 4}
{**d0, **d1}
# -

# later keys have precedence
{**d0, **d1, "a": 0}

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## I/O
#
# - text file formats (read using parsers):
#   - delimited files: `CSV`, `TSV`
#   - files with nested data: `JSON`, `XML`, `YAML`
#   - genomics: `FASTA` (DNA sequence), `VCF` (variant calls)
# - binary formats (dedicated libraries):
#   - advanced compression support (smaller files)
#   - faster (optimised for a common task)
#   - formats: `HDF5` (hierarchichal), `Parquet` (columnar), `Avro` (row)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# 1. open file: read, write, text, binary
# 2. do operations: read, write, seek
# 3. close file (otherwise may get corrupted)
# 4. Standard library: `csv`, `json`, `xml`, `yaml`, `zip`, `bz2`

# + {"slideshow": {"slide_type": "subslide"}}
txt = open("/tmp/afile.txt", mode="w")
txt.write("foo")
txt.write("bar")
txt.write("baz\n")
txt.write(str(1) + "\n")
txt.close()
# -

# ! cat /tmp/afile.txt

# + {"slideshow": {"slide_type": "subslide"}}
txt = open("/tmp/afile.txt", mode="r")  # open
for line in txt.readlines():  # work with it
    print(line)

# + {"slideshow": {"slide_type": "fragment"}}
txt.close()  # close

# + {"slideshow": {"slide_type": "fragment"}}
# why the extra lines?

# + {"slideshow": {"slide_type": "subslide"}}
# use context managers
with open("/tmp/afile.txt", mode="w") as txt:
    txt.write("foo")
    txt.write("bar")
    txt.write("baz\n")
    txt.write(str(42) + "\n")
# -

# ! cat /tmp/afile.txt

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Advanced example from tutorial helpers
# -

from tutorial.io import read_file

# + {"slideshow": {"slide_type": "subslide"}}
read_file??

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# <center><strong>&#9646;&#9646;</strong></center>

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Problem 1, attempt 2
#
# - Read a sequence, and count the number of bases of each type.
# - Print out the counts as a table, or write it to a CSV file.
# -



# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Problem 2, attempt 2
#
# - Read a sequence, and identify the sequence of *Codons*.
# - Print out the position and codon as a table, or write it to a CSV file.
# -



# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Problem 3
#
# - read `data/summary.txt` as a "table", and summarise the data
# - *Note:* you might need to do some cleaning, to interpret the table as numbers
# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# <center><strong>&#9654;</strong></center>

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # ![Python logo](data/python.ico) Advanced Python concepts

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Writing scripts
#
#
# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### *shebang* line:
#
#     #!/usr/bin/python
#     # script continues ...
#
# or more portable:
#
#     #!/usr/bin/env python
#     # script continues ...
# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### `import` statements
#
# **Syntax:** `import module` or `from module import name [, name]`
# -
import sys  # module name
from pathlib import Path  # function or class name
from functools import chain, accumulate  # multiple names

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Argument parsing
# -
sys.argv  # all command line arguments (including script name)


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Problem 1, attempt 3
#
# - Read a sequence, and count the number of bases of each type.
# - Print out the counts as a table, or write it to a CSV file.
# - Write the solution as a script that takes a fasta sequence file as argument
# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# *Tips:* use libraries like,
# - `argparse` (in the standard library, no installation needed),
# - `click` (external library, more concise *decorator* based API).
#
# *Solutions:* see [simple](prob-1-soln-1.py), [more complete](prob-1-soln-2.py).
# -



# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Decorators
#
# - Allows you to modify behaviour by "wrapping" an existing function
# - They are functions themselves
# + {}
def make_bold(fn):
    def wrapper(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapper

@make_bold
def hello1():
    return "Hello World!"


# -


hello1()


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# *How does it work?*

# +
@make_bold
def hello1(name="World"):
    return f"Hello {name}!"

def hello2(name="World"):
    return f"Hello {name}!"
hello2 = make_bold(hello2)  # equivalent
# -

hello2("Foo"), hello3("Bar")

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Reimplement retaining the function name

# +
from functools import wraps

def makebold(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapper

@makebold
def hello2(name="World"):
    return f"Hello {name}!"


# -

hello1.__name__, hello2.__name__


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Decorators with parameters

# +
def format_tag(tag):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return f"<{tag}>{fn(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

@format_tag("b")
def hello1(name="World"):
    return f"Hello {name}!"

@format_tag("i")
def hello2(name="World"):
    return f"Hello {name}!"


# -

hello1("Felix"), hello2("Phoenix")

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Generators
#
# - functions with lazy evaluation
# - `yield` -> `return`


# + {"slideshow": {"slide_type": "fragment"}}
def myrange(start, end, step=1):
    """My range implementation"""
    res = start
    while res < end:
        yield res
        res += step


# -

[i for i in myrange(0, 10, 3)]

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Iterators & generator expressions
#
# - represents a stream of data, but returns one element at a time
# - can be used in a `for`-loop like a container
# - more efficient
# -
lst_iter = iter([1, 2, 3])
a = next(lst_iter)  # get next element
b, c = lst_iter     # unpack all elements
a, b, c


# + {"slideshow": {"slide_type": "fragment"}}
import sys

lst = [i/2 for i in range(1_000_000)]
lst_itr = (i/2 for i in range(1_000_000))
sys.getsizeof(lst), sys.getsizeof(lst_itr)  # size in bytes

# + {"slideshow": {"slide_type": "fragment"}}
sys.getsizeof(lst), sys.getsizeof(list(lst_itr))  # size in bytes

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Other built-ins to create iterators
#
# - `zip` "ties" two iterables
# - `enumerate` with index

# + {"slideshow": {"slide_type": "subslide"}}
vowels = ("a", "e", "i", "o", "u")
for vowel, num in zip(range(len(vowels)), vowels):
    print(vowel, num)

# + {"slideshow": {"slide_type": "subslide"}}
for index, vowel in enumerate(vowels):
    print(index, vowel)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Using `lambda` functions with `map`, `all`, `any`
#
# *Note:* `map` returns an iterator
#
# - split the strings to a pair of numbers: `["1,2", ..]` -> `[[1, 2], ..]`
#   - flatten the result
# -

pairs = ["1,2", "3,4", "5,6"]

# + {"slideshow": {"slide_type": "fragment"}}
res = list(map(lambda i: list(map(int, i.split(","))), pairs))
res

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# *Hints:*
# - `map` and `list.extend` or nested for loop
# - `itertools.chain` or `itertools.chain.from_iterable` (returns an iterator)
# - `functools.reduce`
# -



# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# *Solutions*
# -

flat = []
_ = list(map(flat.extend, res))
flat

# + {"slideshow": {"slide_type": "fragment"}}
import itertools

list(itertools.chain.from_iterable(res))

# + {"slideshow": {"slide_type": "fragment"}}
from functools import reduce

reduce(lambda i, j: i + j, res)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# *Advanced variation of reduce*

# +
from itertools import accumulate
from operator import add

list(accumulate(res, add))

# +
# play around here

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# - in a random sequence of characters, find
#   - if any of them are vowels,
#   - if all of them are vowels,
#   - count vowels

# + {"slideshow": {"slide_type": "subslide"}}
from random import choices
from string import ascii_lowercase

vowels = ("a", "e", "i", "o", "u")
population = choices(ascii_lowercase, k=10)  # `k` random characters

# + {"slideshow": {"slide_type": "fragment"}}
is_vowel = [c in vowels for c in population]
population, is_vowel
# -

any(is_vowel), all(is_vowel), sum(is_vowel)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Playground
#
# - Play around, try different things
# - apart from the standard library, you can also try `numpy` and `pandas`
# -


