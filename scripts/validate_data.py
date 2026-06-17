#!/usr/bin/env python3
"""Repo data validation for the Boxabl Foundations Guide.

Checks:
  1. Every YAML file in data/ parses cleanly.
  2. data/foundation-intake.schema.json is a valid JSON Schema (Draft 2020-12).
  3. data/examples/intake-valid.json validates against the schema.
  4. data/examples/intake-invalid.json is REJECTED by the schema.
  5. Every relative markdown link in the repo resolves to a real file.

Exit code 0 = clean, 1 = problems found. Run from anywhere:
    python scripts/validate_data.py
"""

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
problems: list[str] = []
checks = 0


def ok(msg: str) -> None:
    print(f"  PASS  {msg}")


def fail(msg: str) -> None:
    problems.append(msg)
    print(f"  FAIL  {msg}")


# --- 1. YAML parses -----------------------------------------------------------
print("\n[1/5] YAML files parse")
for path in sorted((ROOT / "data").glob("*.yaml")):
    checks += 1
    try:
        yaml.safe_load(path.read_text(encoding="utf-8"))
        ok(path.relative_to(ROOT).as_posix())
    except yaml.YAMLError as exc:
        fail(f"{path.relative_to(ROOT)}: {exc}")

# --- 2. Schema is a valid JSON Schema -----------------------------------------
print("\n[2/5] Intake schema is a valid Draft 2020-12 schema")
schema_path = ROOT / "data" / "foundation-intake.schema.json"
checks += 1
schema = None
try:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    ok(schema_path.relative_to(ROOT).as_posix())
except Exception as exc:  # noqa: BLE001 - report anything
    fail(f"{schema_path.relative_to(ROOT)}: {exc}")

# --- 3 & 4. Fixtures behave as labeled -----------------------------------------
print("\n[3/5] Valid fixture passes schema")
if schema is not None:
    validator = Draft202012Validator(schema)

    checks += 1
    valid_path = ROOT / "data" / "examples" / "intake-valid.json"
    try:
        valid_doc = json.loads(valid_path.read_text(encoding="utf-8"))
        errs = sorted(validator.iter_errors(valid_doc), key=lambda e: e.json_path)
        if errs:
            for e in errs:
                fail(f"intake-valid.json should pass but failed at {e.json_path}: {e.message}")
        else:
            ok("data/examples/intake-valid.json validates")
    except Exception as exc:  # noqa: BLE001
        fail(f"{valid_path.relative_to(ROOT)}: {exc}")

    print("\n[4/5] Invalid fixture is rejected by schema")
    checks += 1
    invalid_path = ROOT / "data" / "examples" / "intake-invalid.json"
    try:
        invalid_doc = json.loads(invalid_path.read_text(encoding="utf-8"))
        errs = list(validator.iter_errors(invalid_doc))
        if errs:
            ok(f"data/examples/intake-invalid.json correctly rejected ({len(errs)} violations)")
        else:
            fail("intake-invalid.json unexpectedly PASSED validation - schema may be too loose")
    except Exception as exc:  # noqa: BLE001
        fail(f"{invalid_path.relative_to(ROOT)}: {exc}")
else:
    print("  SKIP  fixtures (schema failed to load)")

# --- 5. Internal markdown links resolve ----------------------------------------
print("\n[5/5] Internal markdown links resolve")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")
link_failures = 0
for md in sorted(ROOT.rglob("*.md")):
    if "node_modules" in md.parts or ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8", errors="replace")
    for raw in LINK_RE.findall(text):
        if raw.startswith(SKIP_PREFIXES):
            continue
        target = raw.split("#", 1)[0]
        if not target:
            continue
        checks += 1
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            link_failures += 1
            fail(f"{md.relative_to(ROOT)} -> broken relative link: {raw}")
if link_failures == 0:
    ok("all relative links resolve")

# --- Summary -------------------------------------------------------------------
print(f"\n{'=' * 60}")
if problems:
    print(f"VALIDATION FAILED: {len(problems)} problem(s) across {checks} checks")
    sys.exit(1)
print(f"ALL CHECKS PASSED ({checks} checks)")
sys.exit(0)
