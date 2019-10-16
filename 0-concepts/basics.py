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
# ---

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Getting familiar with the basics

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

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
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

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Booleans

# + {"slideshow": {"slide_type": "-"}}
eq = p == 10000
eq, type(eq)

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# #### Boolean operations
# -

-2 > 3 or -1 < 0, 2 > 3 and -1 > 3, not True

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Strings

# + {"slideshow": {"slide_type": "-"}}
txt = "foo bar baz"
txt, type(txt)

# + {"slideshow": {"slide_type": "fragment"}}
# escaping, and nested quotes
"Don't be an ass", "Don't be an ass"

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Strings

# + {"slideshow": {"slide_type": "-"}}
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

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# #### String operations

# + {"slideshow": {"slide_type": "-"}}
# multiply
"--8<-" * 5

# + {"slideshow": {"slide_type": "fragment"}}
# in
"foo" in "foo bar baz"


# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### User defined types

# + {"slideshow": {"slide_type": "-"}}
class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass("{self.name}")'


instance = MyClass("foo")

instance, type(instance)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Containers

# + {"slideshow": {"slide_type": "-"}}
l = [x, y, p, q, txt, eq]
l, type(l)

# + {"slideshow": {"slide_type": "fragment"}}
t1 = (x, y, eq)
t1, type(t1)
# -

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
# -

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

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
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
True if "fool" not in txt else False

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ### Iteration
# -

# iterate over items
for i in l:
    print(i)

# + {"slideshow": {"slide_type": "fragment"}}
# iterate by index
for i in range(len(l)):
    print(l[i])
# -

# ### Iteration

# + {"slideshow": {"slide_type": "subslide"}}
# flexible
i = 0
res = []
while i < len(txt):
    res += [txt[-1 - i]]
    i += 1
"".join(res)  # calling: str.join(iterable)
# -
