# USD Sidecar Tools

These tools are only needed for binary `.usdc` export and USD validation. Direct
`.usda` export from TouchDesigner does not need usd-core.

## Setup

```powershell
python tools/setup.py
```

The setup script creates `tools/.venv-usd` with Python's built-in `venv` module and
installs the pinned packages from `tools/requirements.txt`. Use `--force` to rebuild:

```powershell
python tools/setup.py --force
```

Inside TouchDesigner, press `Setup Binary Support` on `TD_SOP_USD_Anim_Bridge` to run the
same setup with TD's bundled Python. The setup needs internet access for `pip`.

## Interpreter Selection

`.usdc` transcode uses the first valid Python in this order:

1. `USD Python Executable` custom parameter on the component.
2. `TD_SOP_USD_ANIM_BRIDGE_PYTHON` environment variable.
3. `tools/.venv-usd` created by `tools/setup.py`.

The selected interpreter is a Python executable file, not a package folder. It must
have `usd-core` installed. On Windows this usually ends with `python.exe`, for
example `tools/.venv-usd/Scripts/python.exe`.

## Commands

```powershell
tools/.venv-usd/Scripts/python.exe tools/validate_usd.py export/sop_usd_export.usda
tools/.venv-usd/Scripts/python.exe tools/transcode_usd.py input.usda output.usdc
```

On macOS/Linux, use `tools/.venv-usd/bin/python` instead of `Scripts/python.exe`.

## Version Pin

`tools/requirements.txt` currently pins `usd-core==26.5`, matching the sidecar used
to validate and transcode the project examples.
