# dbt-subdocs

<div align="center">

[![Build status](https://github.com/jb-delafosse/dbt-subdocs/workflows/build/badge.svg?branch=master&event=push)](https://github.com/jb-delafosse/dbt-subdocs/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/dbt-subdocs.svg)](https://pypi.org/project/dbt-subdocs/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jb-delafosse/dbt-subdocs/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/jb-delafosse/dbt-subdocs/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/jb-delafosse/dbt-subdocs/releases)
[![License](https://img.shields.io/github/license/jb-delafosse/dbt-subdocs)](https://github.com/jb-delafosse/dbt-subdocs/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

dbt-subdocs is a python CLI you can used to generate a dbt-docs for a subset of your dbt project

</div>

## 🤔 Description

This project is useful if you want to generate a dbt-docs site for a subset of the models in your DBT project.
By default, in dbt-docs, all your projects gets documented : 
- all the models
- all the sources
- all the tests
- and all the macros

This CLI is useful if you only want to document what your end-user will be using.

This CLI simply edits the `manifest.json` and `catalog.json` used by the dbt-docs site so they do not
contain nodes you don't want to display.

## ✨ Features

- Configure an input and output directory
- Select the models to document using tag within DBT
- Choose to exclude nodes that are useless for your users : tests, macros, seed etc...

## 🏃 Getting Started


<details>
  <summary>Installation with pip</summary>

```bash
pip install -U dbt-subdocs
```

Then you can run

```bash
dbt-subdocs --help
```
</details>

<details>
  <summary>First call to the CLI</summary>

  You can call dbt-subdocs by simply using the command `dbt-subdocs`
  See all the options available using `dbt-subdocs --help`
</details>

<details>
  <summary>Usecase 1: Only display nodes with a specific tag</summary>

  Assuming your `manifest.json` and `catalog.json` are in `DIRECTORY`, simply call
  ```bash
  cd DIRECTORY
  dbt-subdocs --tag finance
  ```

  If you want to select nodes with tags `finance` OR `engineering`, simply call
  ```bash
  dbt-subdocs --tag finance --tag engineering
  ```
</details>

<details>
  <summary>Usecase 2: Removing macros from the docs</summary>

  If you want to remove macros from the `manifest.json` you can call 
  ```bash
  dbt-subdocs --tag finance --exclude-node-type macros
  ```
  You can also remove sources by using 
  ```bash
  dbt-subdocs --tag finance --exclude-node-type macros --exclude-node-type sources
  ```
</details>

## 🛡️ License

[![License](https://img.shields.io/github/license/jb-delafosse/dbt-subdocs)](https://github.com/jb-delafosse/dbt-subdocs/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/jb-delafosse/dbt-subdocs/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{dbt-subdocs,
  author = {jb-delafosse},
  title = {dbt-subdocs is a python CLI you can used to generate a dbt-docs for a subset of your dbt project},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/jb-delafosse/dbt-subdocs}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
