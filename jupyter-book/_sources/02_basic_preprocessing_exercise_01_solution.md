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

# Solution for Exercise 01

The goal of is to compare the performance of our classifier to some baseline classifier that  would ignore the input data and instead make constant predictions:

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

high_revenue_clf = DummyClassifier(strategy="constant",
                                   constant=" >50K")
scores = cross_val_score(high_revenue_clf, data_numeric, target)
print(f"{scores.mean():.3f} +/- {scores.std():.3f}")
```

```{code-cell}
low_revenue_clf = DummyClassifier(strategy="constant",
                                  constant=" <=50K")
scores = cross_val_score(low_revenue_clf, data_numeric, target)
print(f"{scores.mean():.3f} +/- {scores.std():.3f}")
```

```{code-cell}
most_freq_revenue_clf = DummyClassifier(strategy="most_frequent")
scores = cross_val_score(most_freq_revenue_clf, data_numeric, target)
print(f"{scores.mean():.3f} +/- {scores.std():.3f}")
```

So 81% accuracy is significantly better than 76% which is the score of a baseline model that would always predict the most frequent class which is the low revenue class: `" <=50K"`.

In this dataset, we can see that the target classes are imbalanced: almost 3/4 of the records are people with a revenue below 50K:

```{code-cell}
df["class"].value_counts()
```

```{code-cell}
(target == " <=50K").mean()
```
