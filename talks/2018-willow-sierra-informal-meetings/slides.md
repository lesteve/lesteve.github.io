## Python guidelines 101  <!-- .element style="text-align: center; margin-left: 0px" -->
<!-- ### a machine learning toolkit in Python  <\!-- .element text-align: center; margin-left: 0px" -\-> -->


------

### Loïc Estève <!-- .element style="text-align: center; margin-left: 0px" -->

<div style="text-align: center; margin-top: 100px">
  <img src="img/inria.png" alt="Inria" height="120px"/>
</div>

==

## Quick bio

* background in experimental Particle Physics (PhD + post-doc)  <!-- .element class="fragment" -->
* research developer quantitative hedge fund (Winton Capital). Mostly C++ and
  as much Python as I could.  <!-- .element class="fragment" -->
* Parietal team at Inria Saclay. Work on Python open-source
  software: mostly scikit-learn, joblib, nilearn, sphinx-gallery. <!-- .element class="fragment" -->

==

## Outline

* Python Install
* Recommendation for editors
* Python 2 vs Python 3
* Jupyter notebook
* How can I improve your life?

Ask questions, shout if you disagree!

<small>
Most of this is advice I would give to someone starting with Python</br>
If you do things differently and that works for you, by all means keep doing it!</br>
If you think this is better that my recommendations, do let me know!
</small>

==

## Python install

Install [miniconda](https://conda.io/miniconda.html) Python 3 64-bit.

```bash
# install packages
conda install pytorch=0.3.1 ipython

# create conda environments
conda create -n env-name python=2 scikit-learn

# activate/deactivate environment
source activate env-name
source deactivate
```

Use conda when you can, pip when you have to.

conda is not only for Python packages

conda-forge channel can be handy
(community-based so wider range of available packages)

Avoid mixing conda and pip for a single package.

==

## Editors: features

Musts:
* tabs = 4 spaces
* indent/dedent blocks
* "while you type" flake8

Nice to have:
* automatic completion
* easy access to the doc
* easy way to go to the function definition
* run (parts of a) file in a interactive console

==

## Editors: a few good choices

* Visual Studio code or Atom. Need to install additional plugins to have some
  of the features above.
* PyCharm: IDE, a bit more heavy-weight.

Play with them and see the ones you prefer</br>
Ask around what people use and why.

<small>
If you happen to use emacs, do ask me about my config after the meeting
</small>


==

## Python 2 vs Python 3

No reason to stick with Python 2: all the main libraries have supported Python
3 for a few years (numpy ~8 years, scikit-learn ~5 years, matplotlib ~5 years) <!-- .element class="fragment" -->

In practice not so much difference for scientific computing: print is a
function, a few things produce iterators rather than lists, e.g. map. <!-- .element class="fragment" -->

If you still have projects that use Python 2, you can create a conda
environment with Python 2. <!-- .element class="fragment" -->

==

## Python 2 vs Python 3: carrots

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

==

## Python 2 vs Python 3: sticks

* January 2020: Python 2 support end of life
* April 2017: IPython 6.0 is Python 3 only
* January 2019: Numpy new releases will be Python 3 only
* January 2020: Plenty of projects (pandas, matplotlib, Jupyter notebook, astropy, ...) will
  drop support for Python 2 https://python3statement.org/

==

## Jupyter notebook

Great for mixing code, text, maths and plots. Great for interactive
exploration, teaching/tutorials.

Rendered on github. Easily export to html and send that to your
coworkers.

**Best practice**: move functions to a module once they are reusable and import your
module in your notebook.

<div style="font-size: 75%">
Use [nbdime](http://nbdime.readthedocs.io/en/stable/) for diffs</br>
Try out [Jupyter Lab](http://jupyterlab.readthedocs.io/en/stable/)</br>
Julia and R kernels</br>
[Colaboratory](https://colab.research.google.com) Jupyter notebooks in Google drive.
</div>

==

## sys.path hacking

Do not do this:
```python
# my_module.py
sys.path.append('but/this/works/fine/on/my/machine')
```

Quick and dirty/lazy: put your module in the current directory. Tweak
PYTHONPATH as a one-off <small>(if you really have to)</small>

Right way to do it: write a setup.py. Not that hard
for a pure Python package, see [commented
example](https://github.com/pypa/sampleproject/blob/master/setup.py)

<small>
if something is optional and you don't understand what it does in less than 30
seconds, that probably means you do not need it
</small>

==

## Possible topics for tutorials

* introduction of the Python scientific ecosystem
* profiling Python code
* optimization with cython + numba
* visualization: matplotlib/seaborn/etc ...
* best practices when open-sourcing a package

Anything else? Suggestions more than welcome!

==

## Some of the things I will work on

that may hopefully make your life easier!


### Cluster <!-- .element style="margin-top: 80px" -->

[dask](https://dask.pydata.org/en/latest/) on the
cluster. Will need guinea pigs!

### Experiment management <!-- .element style="margin-top: 50px" -->

Feed-back on [sacred](https://github.com/IDSIA/sacred)?

Feed-back on
[TensorBoard](https://github.com/tensorflow/tensorboard) and
[Visdom](https://github.com/facebookresearch/visdom)?

==

## Grab me and ask questions!

* Complain loudly about your problems/pain points <!-- .element class="fragment" -->
* Anything goes: Python, git, generic programming problems/questions! <!-- .element class="fragment" -->
* Very likely: I won't have an answer to everything right away but I will try! <!-- .element class="fragment" -->
* It will help me understand your needs better and direct my efforts <!-- .element class="fragment" -->
