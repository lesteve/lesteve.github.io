---
jupytext:
  formats: python_scripts//py:percent,notebooks//ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.9'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: scikit-learn-tutorial
---

#  Exercise 01

The goal of is to compare the performance of our classifier (81% accuracy) to some baseline classifiers that  would ignore the input data and instead make constant predictions.

The online [documentation for DummyClassifier](https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators) gives instructions on how to use it.

```{code-cell}
import pandas as pd

df = pd.read_csv(
    "https://www.openml.org/data/get_csv/1595261/adult-census.csv")
```

```{code-cell}
target_name = "class"
target = df[target_name].to_numpy()
data = df.drop(columns=[target_name, "fnlwgt"])
numerical_columns = [
    c for c in data.columns if data[c].dtype.kind in ["i", "f"]]
data_numeric = data[numerical_columns]
```

```{code-cell}
from sklearn.model_selection import cross_val_score
from sklearn.dummy import DummyClassifier

# TODO: write me!
```
