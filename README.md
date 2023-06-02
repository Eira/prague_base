# :WIP: Praha Base


### Pre-requirements
- [python 3.11+](https://www.python.org/downloads/)

### Local setup
```shell
$ git clone git@github.com:esemi/prague_base.git
$ cd canyon-notifier
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
