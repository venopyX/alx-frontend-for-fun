#!/usr/bin/python3
"""
Markdown to HTML Converter

This script converts a markdown file to HTML format.
Usage: ./markdown2html.py <markdown_file> <output_html_file>
"""

import sys


def checkargs():
    """
    Validates input arguments and returns the markdown filename.
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as md_file:
            return md_file.read()
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to handle markdown to HTML conversion.
    """
    content = checkargs()
    sys.exit(0)


if __name__ == "__main__":
    main()
