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
# ![Python logo](data/python-logo-mini.png)
#
# # Hello Python!

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
# ### Numbers

# + {"slideshow": {"slide_type": "-"}}
x, y = 3, 3.0
x, type(x), y, type(y)

# + {"slideshow": {"slide_type": "fragment"}}
p, q = 10_000, 1e4
p, type(p), q, type(q)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Numeric operations

# + {"slideshow": {"slide_type": "-"}}
# increment, similar for most other operators
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
# exponent
3 ** 3

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Booleans

# + {"slideshow": {"slide_type": "-"}}
eq = p == 10000
eq, type(eq)

# + {"slideshow": {"slide_type": "fragment"}}
# numbers and strings: 0, empty string, None -> False, everything else -> True
bool(1), bool(0), bool(""), bool("foo"), bool(None)

# + {"slideshow": {"slide_type": "fragment"}}
# containers: empty -> False, has element -> True
bool(list()), bool([1]), bool(set()), bool({1}), bool(dict()), bool({1: 4})

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# #### Boolean operations
# -

-2 > 3 or -1 < 0, 2 > 3 and -1 > 3, not True

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Strings

# + {"slideshow": {"slide_type": "-"}}
txt = "foo bar baz"
txt, type(txt)

# + {"slideshow": {"slide_type": "fragment"}}
# escaping, and nested quotes
"Don't be an ass", "Don't be an ass"

# + {"slideshow": {"slide_type": "subslide"}}
multi = "First\nSecond"
multi

# + {"slideshow": {"slide_type": "fragment"}}
print(multi)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### String operations

# + {"slideshow": {"slide_type": "-"}}
# concatenation
"foo" "bar"

# + {"slideshow": {"slide_type": "fragment"}}
"foo" "bar"

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
"foo" in "foo bar baz"


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
l = [x, y, p, q, txt, eq]
l, type(l)

# + {"slideshow": {"slide_type": "fragment"}}
t1 = (x, y, eq)
t1, type(t1)

# + {"slideshow": {"slide_type": "subslide"}}
# append
l + [1, 2]

# + {"slideshow": {"slide_type": "fragment"}}
# multiply
t1 * 3

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Indexing and slicing
#
# Syntax: `container[index]`

# + {"slideshow": {"slide_type": "-"}}
l[0] == t1[0] == 3

# + {"slideshow": {"slide_type": "fragment"}}
l[-1] == True

# + {"slideshow": {"slide_type": "subslide"}}
l, l[:2], l[1:3]

# + {"slideshow": {"slide_type": "fragment"}}
l[0:4:2], l[::3]

# + {"slideshow": {"slide_type": "fragment"}}
txt, txt[4:7]

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Mutable and immutable types
#
# Certain types, once created cannot be "edited"; e.g. `str`, `tuple`.

# + {"slideshow": {"slide_type": "fragment"}}
l

# + {"slideshow": {"slide_type": "-"}}
l[0] = p
l

# + {"slideshow": {"slide_type": "subslide"}}
t1

# + {"slideshow": {"slide_type": "fragment"}}
t1[0] = p

# + {"slideshow": {"slide_type": "fragment"}}
txt[5] = "e"

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Flow control
#
# - conditionals
# - iteration
# - routines/functions

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Conditionals
# -

# if .. else ..
if "foo" in txt:
    pass
elif "bar" in txt:  # optional
    pass
else:  # optional
    pass

# + {"slideshow": {"slide_type": "fragment"}}
# ternary conditional
True if "fool" not in txt else False

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Iteration
# -

# iterate over items
for i in l:
    print(i)

# + {"slideshow": {"slide_type": "subslide"}}
# iterate by index
for i in range(len(l)):
    print(l[i])

# + {"slideshow": {"slide_type": "subslide"}}
# flexible iteration
i = 0
res = []
while i < len(txt):
    res += [txt[-1 - i]]
    i += 1
"".join(res)  # calling: str.join(iterable)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ##### `break` and `continue` statements
#
# What does the following do?

# + {"slideshow": {"slide_type": "-"}}
i = 0
while i < len(txt):
    if txt[i] == "b":
        break  # prematurely ends any iteration
    i += 1
txt[:i]

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# **Ans:** *Finds b / Shows the string upto the first b*

# + {"slideshow": {"slide_type": "subslide"}}
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
# ### Functions
#
# - Wraps a code block that can be reused, arguments act as parameters
# - Ends in a `return` statement; returns the control back to the caller

# +
def add(i, j):
    """Adds two numbers"""
    return i + j


def sub(i, j):
    """Subtracts the second number from the first"""
    return i - j


def op(i, j, operator=add):
    """Applies a binary operator to two numbers"""
    return operator(i, j)


# + {"slideshow": {"slide_type": "subslide"}}
op(3, 4)

# + {"slideshow": {"slide_type": "fragment"}}
op(3, 4, sub)

# + {"slideshow": {"slide_type": "fragment"}}
op(3, 4, lambda i, j: i * j)


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### Positional and keyword arguments
# -


def myfunc(pos1, pos2, kw1="foo", kw2="bar"):
    print(pos1, pos2, kw1, kw2)


# + {"slideshow": {"slide_type": "fragment"}}
myfunc(1, 2, 3, 4)
# -

myfunc(1, 2, kw2="random", kw1="order")

myfunc(5, kw1="bla", pos2=99, kw2="dibla")

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# <center><strong>&#9646;&#9646;</strong></center>

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

seq1

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
# ![Python logo](data/python-logo-mini.png)
#
# # More useful Python concepts

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
a = "foo"
b = "bar"
c = "baz"
f"{a} {b} {c} {c.upper()}"

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
# -

set(f"{a} {b} {c}")  # unique elements

# + {"slideshow": {"slide_type": "fragment"}}
a_, b_, c_ = [set(i) for i in (a, b, c)]
# -

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

# + {"slideshow": {"slide_type": "fragment"}}
{k: (v, v < 5) for k, v in week.items()}

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Function calls
# -

# ### Arbitrary arguments


# ### Argument unpacking


# ### Generators
#
# Use `yield` instead of `return`


def myrange(start, end, step=1):
    """A range implementation"""
    res = start
    while res < end:
        yield res
        res += step


[i for i in myrange(0, 10, 3)]
