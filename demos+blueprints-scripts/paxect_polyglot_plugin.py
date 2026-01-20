#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
"""
PAXECT Polyglot Plugin — standalone CLI (no Core required)

Modes:
  - health : quick health probe (no I/O)
  - test   : copies input to output (deterministic smoke test)
  - upper  : uppercase transform (UTF-8 strict)
  - lower  : lowercase transform (UTF-8 strict)

I/O:
  - --input / --output are optional; defaults to stdin/stdout

Exit codes:
  0 OK, 2 I/O error, 3 argument error
"""

import sys, argparse

VERSION = "1.0.1"

def read_bytes(path: str | None) -> bytes:
    try:
        if path:
            with open(path, "rb") as f:
                return f.read()
        return sys.stdin.buffer.read()
    except Exception as e:
        print(f"[error] read failed: {e}", file=sys.stderr)
        sys.exit(2)

def write_bytes(path: str | None, data: bytes) -> None:
    try:
        if path:
            with open(path, "wb") as f:
                f.write(data)
        else:
            sys.stdout.buffer.write(data)
    except Exception as e:
        print(f"[error] write failed: {e}", file=sys.stderr)
        sys.exit(2)

def run(mode: str, inp: str | None, out: str | None) -> int:
    if mode == "health":
        return 0

    data = read_bytes(inp)

    if mode == "test":
        out_bytes = data
    elif mode in ("upper", "lower"):
        try:
            txt = data.decode("utf-8", errors="strict")
        except UnicodeDecodeError as e:
            print(f"[error] utf-8 decode failed: {e}", file=sys.stderr)
            return 2
        out_bytes = (txt.upper() if mode == "upper" else txt.lower()).encode("utf-8")
    else:
        print(f"[error] unsupported mode: {mode}", file=sys.stderr)
        return 3

    write_bytes(out, out_bytes)
    return 0

def main() -> int:
    p = argparse.ArgumentParser(
        prog="paxect_polyglot_plugin",
        description="Standalone PAXECT Polyglot plugin (plug & play)."
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    p.add_argument("--mode", required=True, choices=["health","test","upper","lower"])
    p.add_argument("--input","-i", help="Input file (default: stdin)")
    p.add_argument("--output","-o", help="Output file (default: stdout)")
    args = p.parse_args()
    return run(args.mode, args.input, args.output)

if __name__ == "__main__":
    sys.exit(main())
