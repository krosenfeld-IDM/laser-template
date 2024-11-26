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

For linting you find it useful to intall [pre-commit](https://pre-commit.com/) and [ruff](https://docs.astral.sh/ruff/) and then, before committing to github, running:

```
pre-commit run --all-file
ruff check
ruff check --fix
```
