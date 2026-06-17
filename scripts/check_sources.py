#!/usr/bin/env python3
"""Source freshness checker for the Boxabl Foundations Guide.

Reads data/SOURCES.yaml, requests every URL, and reports:
  - DEAD     : non-2xx/3xx response or connection failure
  - STALE    : checked_on older than STALE_DAYS (default 180)
  - OK       : reachable and recently verified

Exit code 1 if any source is DEAD, so a scheduled CI job fails loudly and
notifies the maintainer. Stale sources warn but do not fail the job.

Run: python scripts/check_sources.py
Uses only the standard library plus PyYAML.
"""

import sys
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
STALE_DAYS = 180
TIMEOUT = 20
UA = (
    "Mozilla/5.0 (compatible; BoxablFoundationsGuide-LinkCheck/1.0; "
    "+https://boxablfoundations.com)"
)


def probe(url: str) -> tuple[bool, str]:
    """Return (reachable, detail). Tries HEAD first, falls back to GET."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                return True, f"HTTP {resp.status}"
        except urllib.error.HTTPError as exc:
            if method == "GET":
                # Some CDNs reject HEAD; a GET 403/405 is still a real answer.
                return (200 <= exc.code < 400), f"HTTP {exc.code}"
        except Exception as exc:  # noqa: BLE001
            if method == "GET":
                return False, f"{type(exc).__name__}: {exc}"
    return False, "unreachable"


def main() -> int:
    registry = yaml.safe_load((ROOT / "data" / "SOURCES.yaml").read_text(encoding="utf-8"))
    sources = registry.get("sources", [])
    today = date.today()
    dead, stale = [], []

    print(f"Checking {len(sources)} sources from data/SOURCES.yaml\n")
    for src in sources:
        sid, url = src.get("id", "?"), src.get("url", "")
        if not url or src.get("type") == "internal":
            print(f"  SKIP   {sid}")
            continue

        reachable, detail = probe(url)
        checked_on = src.get("checked_on")
        age_note = ""
        if checked_on:
            checked = (
                checked_on
                if isinstance(checked_on, date)
                else datetime.strptime(str(checked_on), "%Y-%m-%d").date()
            )
            age = (today - checked).days
            age_note = f" (verified {age}d ago)"
            if age > STALE_DAYS:
                stale.append(sid)

        if reachable:
            print(f"  OK     {sid}: {detail}{age_note}")
        else:
            dead.append(sid)
            print(f"  DEAD   {sid}: {detail} -> {url}")

    print(f"\n{'=' * 60}")
    if stale:
        print(f"STALE ({len(stale)}): re-verify content for: {', '.join(stale)}")
    if dead:
        print(f"DEAD ({len(dead)}): fix or replace: {', '.join(dead)}")
        return 1
    print("All sources reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
