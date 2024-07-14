# Task 1

To run the code, use the following command:

```sh
python -mtask1 ./task1.txt

```

## usage

To see the usage of the code, use the following command:

```sh
python -mtask1 -h
usage: __main__.py [-h] path

positional arguments:
  path        Path to the file

options:
  -h, --help  show this help message and exit
```

# Task 2

To run the code, use the following command:

```sh
python -mtask2 ./task2.txt

```

## usage

To see the usage of the code, use the following command:

```sh
python -mtask2 -h
usage: __main__.py [-h] path

positional arguments:
  path        Path to the file

options:
  -h, --help  show this help message and exit
```

# Tests

To run the tests, use the following command:

```sh
poetry env use `which python`
poetry install --no-root
poetry run pytest -vx tests
```
