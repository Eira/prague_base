# :WIP: Praha Base

[![tests](https://github.com/Eira/prague_base/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/Eira/prague_base/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/Eira/prague_base/branch/master/graph/badge.svg?token=DDGHRUZZ0P)](https://codecov.io/github/Eira/prague_base)
[![linters](https://github.com/Eira/prague_base/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/Eira/prague_base/actions/workflows/linters.yml)

### Pre-requirements
- [python 3.11+](https://www.python.org/downloads/)

### Local setup
```shell
$ git clone git@github.com:esemi/prague_base.git
$ cd prague_base
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry pip setuptools
$ poetry config virtualenvs.create false --local
$ poetry install
```

### Local run tests
```shell
$ pytest --cov=app
```

### Local run linters
```
poetry run flake8 app/

poetry run mypy app/
```

### Set up crontab
```
crontab -r etc/crontab.txt
```