# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Getting familiar with the basics

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Python: history and now
#
# - Created by Guido van Rossum in 1990.  At the time he was a postdoc at CWI, Amsterdam, currently he is at Dropbox.
# - Named after **Monty Python**, Guido is a big fan.
# - Development guided by the Python Steering Council, entirely community led effort, supported by the Python Software Foundation.

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## The Python ecosystem
#
# - Ease of use among its primary considerations
# - Highly extendable, including through extensions written in lower level languages like C/C++.
# - Natively there are certain performance limitations (e.g. *Global Interpreter Lock (GIL)*), but effectively not a limitation as it can be worked around with extensions:
#   `numpy`, `xarray`, `pandas`, `numba`, `pyarrow`, etc.
# - Writing *native* extensions is easier with `Cython` (Python + type information)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Understanding variables
#
# Variables hold a *reference* to a value,
# - can be *objects* of simple *types* (e.g. numbers, strings, booleans),

# + {"slideshow": {"slide_type": "subslide"}}
x, y = 3, 3.0
x, type(x), y, type(y)

# + {"slideshow": {"slide_type": "fragment"}}
p, q = 10_000, 1e4
p, type(p), q, type(q)

# + {"slideshow": {"slide_type": "subslide"}}
eq = p == 10000
eq, type(eq)

# + {"slideshow": {"slide_type": "fragment"}}
txt = "foo bar baz"
txt, type(txt)


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# - user defined types,

# + {"slideshow": {"slide_type": "fragment"}}
class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass("{self.name}")'


instance = MyClass("foo")

instance, type(instance)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# - *sequences* or *containers* (contains other variables), and others (esp. in Python).

# + {"slideshow": {"slide_type": "fragment"}}
l = [x, y, p, q, txt, eq]
l

# + {"slideshow": {"slide_type": "subslide"}}
t1 = x, y, eq
t1

# + {"slideshow": {"slide_type": "fragment"}}
t2 = (x, y, eq)
t2

# + {"slideshow": {"slide_type": "fragment"}}
type(l), type(t1), type(t2)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Indexing and slicing
#
# Syntax: `container[index]`

# + {"slideshow": {"slide_type": "fragment"}}
l[0] == t1[0] == 3

# + {"slideshow": {"slide_type": "fragment"}}
l[-1] == True

# + {"slideshow": {"slide_type": "subslide"}}
l, l[:2], l[1:3]

# + {"slideshow": {"slide_type": "fragment"}}
l[0:4:2], l[::3]

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Mutable and immutable types
#
# Certain types, once created cannot be "edited"; e.g. `str`, `tuple`.

# + {"slideshow": {"slide_type": "fragment"}}
l[0] = p
l

# + {"slideshow": {"slide_type": "subslide"}}
t1[0]

# + {"slideshow": {"slide_type": "fragment"}}
t1[0] = p

# + {"slideshow": {"slide_type": "subslide"}}
txt[5]

# + {"slideshow": {"slide_type": "fragment"}}
txt[5] = "e"
# -

# ## Flow control
#
#
