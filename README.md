# laser-template
Template for producing models implemented with the LASER toolkit.

## Setup
Example using [uv](https://github.com/astral-sh/uv):

0. Create and activate virtual environment
```
uv venv
source .venv/bin/activate
```
1. Install
```
uv pip install -e .
```
2. Test that the model runs (`laser --help` for options)
```
laser
```

## Development notes

To run all tests:

```
tox
```