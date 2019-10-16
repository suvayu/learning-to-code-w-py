%.ipynb:	%.py
	jupytext -o $@ --to "ipynb:light" $<
	touch $<

%.py:	%.ipynb
	jupytext -o $@ --to "py:light" $<
	black -l 79 $@
