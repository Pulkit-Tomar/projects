import py_compile
from pathlib import Path

root = Path(__file__).parent
py_files = sorted(root.glob("*.py"))
failures = []

print("Checking Python syntax for all .py files in the workspace...")
for path in py_files:
    if path.name == Path(__file__).name:
        continue
    try:
        py_compile.compile(path, doraise=True)
        print(f"OK: {path.name}")
    except py_compile.PyCompileError as exc:
        print(f"ERROR: {path.name}")
        print(exc)
        failures.append(path.name)

if failures:
    print(f"\n{len(failures)} file(s) failed syntax check.")
    raise SystemExit(1)

print("\nAll checked files are syntactically valid.")
