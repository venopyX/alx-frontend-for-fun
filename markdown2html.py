#!/usr/bin/python3
"""
Markdown to HTML Converter

This script converts a markdown file to HTML format.
Usage: ./markdown2html.py <markdown_file> <output_html_file>
"""

import sys


def main():
    """
    Main function to handle markdown to HTML conversion.
    Validates input arguments and reads the markdown file.
    """
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


if __name__ == "__main__":
    main()
