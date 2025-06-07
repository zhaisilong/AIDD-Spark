# AIDD-Spark

Jupyter Notebook Tutorial for AIDD Beginners

## Setups

```bash
git clone git@github.com:zhaisilong/AIDD-Spark.git
cd AIDD-Spark

mamba create -n aidd-spark python=3.10
mamba activate aidd-spark
mamba install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1  pytorch-cuda=11.8 -c pytorch -c nvidia

# Install dependencies
pip install -e .
```

## Build the book

This tutorial is built with [Jupyter Book](https://next.jupyterbook.org/start).

```bash
jupyter book init  # this will install node.js and other dependencies into ~/.local/share/jupyter-book
jupyter book init --write-toc
jupyter book init --gh-pages  # this will create a new directory called _build/html/

jupyter book start
```

```bash
jupyter book templates list --pdf
```

```bash

```
