.. image:: data/python-logo-mini.png

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/suvayu/learning-to-code-w-py/master

Learning to program, with Python
================================

This repo holds the content I wrote for a mini workshop to teach a
group of graduate students, consisting mostly of biologists with very
little exposure to programming, how to code.  They needed programming
to analyse datasets that vary from DNA sequences, typical statistical
data, and some basic language processing.  The initial feedback from
the students was: "We don't know where to begin".  So, in this
tutorial my goal was to make them comfortable with basic programming
idioms, and a very short primer on how to use libraries (mostly the
standard library) to do more complex tasks.

To go through the content, just click on the "launch binder" button,
which should take you to mybinder.org.  Initially you might need to
wait a while for the image to be created.  Once done, and a jupyter
server is running, you may click on the notebook `concepts.ipynb` and
explore away.

Slides, Setup, & Datasets
-------------------------

While writing the tutorial, I versioned the notebook by syncing it
with a python file using `jupytext
<https://jupytext.readthedocs.io/en/latest/>`_.  You may use the
``Makefile`` to generate the notebook from the python file (or vice
versa).  If you work on the notebook directly, you could sync it with
the python file using the jupyter integration provided by
``jupytext``.  I have used the ``light`` syntax.  I use `RISE
<https://rise.readthedocs.io/>`_ to present the notebook as
interactive slides during the tutorial.

 *Note:* possibly due to a bug in the Jupyter integration of
 ``jupytext``, I could not sync my configurations for RISE to the
 python file.  Since this was one line, I simply fixed this manually.

I have a small helper library under ``tutorial``.  So that imports
work without fiddling with ``sys.path``, it is advised to do the
exercises and run the notebook from the top-level directory.

I have also included a few small datasets under ``data``.  They are:

``example.fa`` : a fasta file from `this Kaggle kernel <https://www.kaggle.com/thomasnelson/working-with-dna-sequence-data-for-ml/data>`__,

``human_ancestor_Y.fa.bz2`` : a compressed fasta file for the Y chromosome from the `1000 Genome Project <http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/technical/reference/ancestral_alignments/>`__ (1KGP),

``summary.txt`` : a TSV file summarising the above dataset from the 1KGP.

``python*.png`` : The image files are from <https://www.python.org/>.

Dependencies
------------

The lesson and exercises uses the standard library, except for the
part where I discuss data analysis libraries like ``numpy``,
``pandas``.  To present the notebook, `RISE`_ is required.  To
sync/generate the notebook `jupytext`_ is required.

Hope this is useful to people out there 😇.

-------

.. image:: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
  :target: https://creativecommons.org/licenses/by-sa/4.0/

This work is licensed under a `Creative Commons Attribution-ShareAlike 4.0 International License <https://creativecommons.org/licenses/by-sa/4.0/>`__.
