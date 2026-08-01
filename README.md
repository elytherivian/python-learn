# python-learn

Python learning examples managed with [uv](https://docs.astral.sh/uv/).

## Quick Start

Clone the repository:

```bash
git clone git@github.com:elytherivian/python-learn.git
cd python-learn
```

Sync dependencies from `uv.lock`:

```bash
uv sync
```

Run the example script:

```bash
uv run python main.py
```

## Notes

- Project metadata is defined in `pyproject.toml`.
- Locked dependency versions are recorded in `uv.lock`.
- After cloning, run `uv sync` first so the local virtual environment matches the lockfile.
