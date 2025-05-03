#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as md_file:
        content = md_file.read()
        sys.exit(0)
except FileNotFoundError:
    print(f"Missing {sys.argv[1]}.", file=sys.stderr)
    sys.exit(1)
