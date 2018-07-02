## Python 2 vs Python 3  <!-- .element style="text-align: center; margin-left: 0px" -->
<!-- ### a machine learning toolkit in Python  <\!-- .element text-align: center; margin-left: 0px" -\-> -->

------

### Loïc Estève <!-- .element style="text-align: center; margin-left: 0px" -->

<div style="text-align: center; margin-top: 100px">
  <img src="img/inria.png" alt="Inria" height="120px"/>
</div>

==

## Outline

### Please use Python 3  <!-- .element class="fragment" -->

<div style="font-size: 80%">
If you are reluctant to switch to Python 3 or have questions about the
migration, let's chat about it at the end of this talk! <!-- .element
class="fragment" -->
</div>

==

## Python 2 vs Python 3

No reason to stick with Python 2: all the main libraries have supported Python
3 for a few years (numpy ~8 years, scikit-learn ~5 years, matplotlib ~5 years) <!-- .element class="fragment" -->

In practice not so much difference for scientific computing: print is a
function, a few things produce iterators rather than lists, e.g. map. <!-- .element class="fragment" -->

If you still have projects that use Python 2, it's completely fine:  <!-- .element class="fragment" -->
* create a conda environment with Python 2   <!-- .element class="fragment" -->
* make your default environment Python 3 and use it for your new projects <!-- .element
class="fragment" -->

==

## Carrots

matrix multiplication
```python
A @ B  # same as np.dot(A, B)
```

f-strings (Python 3.6)
```python
version = 3
msg = f'Please use Python {version} '
msg += f' rather than {version - 1}'
# msg = 'Please use Python 3 rather than 2'
```

true division
```python
x = 3
y = 1/2 * x  # y = 1.5 (y = 0 in Python 2)
```

Faster import from network filesystems (e.g. NFS)

==

## Sticks

* January 2020: Python 2 support end of life  <!-- .element class="fragment" -->
* April 2017: IPython 6.0 Python 3 only, December 2017: Django 2 Python 3 only  <!-- .element class="fragment" -->
* January 2019: Numpy new releases will be Python 3 only  <!-- .element class="fragment" -->
<li class="fragment"> January 2020: Plenty of projects (pandas, matplotlib, Jupyter notebook,
  astropy, ...) will drop support for Python 2 https://python3statement.org/</li>

==

## Summary

#### Please use Python 3

<div style="font-size: 80%">
If you are reluctant to switch to Python 3 or have questions about the
migration, now is a good time to chat!
</div>

==

## Useful links

<!-- .slide: style="font-size: 75%" -->

Simple
[tips](http://python-3-for-scientists.readthedocs.io/en/latest/python3_transition_guide.html)
for migrating to Python 3

Use 2to3 to migrate (as a one-off) from Python 2 to Python 3:
https://docs.python.org/3.6/library/2to3.html

Migrating from Python 2 to Python 2/3 compatible code:
http://python-future.org/automatic_conversion.html

Writing Python 2/3 compatible code:
http://python-future.org/compatible_idioms.html

Python 2 to 3: how to upgrade and what features to start using,
[slides](http://treyhunner.com/2to3/) from PyCon 2018

Core Python developer
[perspective](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html)
on Python 3 migration
