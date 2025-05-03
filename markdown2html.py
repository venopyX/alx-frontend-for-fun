#!/usr/bin/python3
"""
Markdown to HTML Converter

This script converts a markdown file to HTML format.
Usage: ./markdown2html.py <markdown_file> <output_html_file>
"""

import sys
from urllib import parse


def check_args():
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


def parse_headings(content):
    """
    Parses markdown headings and converts them to HTML.
    """
    lines = content.split('\n')
    html_lines = []
    for line in lines:
        if line.startswith('#'):
            level = line.count('#')
            html_line = f"<h{level}>{line[level:].strip()}</h{level}>"
            html_lines.append(html_line)
        else:
            html_lines.append(line)
    return '\n'.join(html_lines)


def parse_unordered_list(content):
    """
    Parses markdown unordered lists and converts them to HTML.
    """
    lines = content.split('\n')
    html_lines = []
    in_list = False
    for line in lines:
        if line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f"<li>{line[1:].strip()}</li>")
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append('</ul>')
    return '\n'.join(html_lines)


def parse_ordered_list(content):
    """
    Parses markdown ordered lists and converts them to HTML.
    """
    lines = content.split('\n')
    html_lines = []
    in_list = False
    for line in lines:
        if line.startswith('* '):
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            html_lines.append(f"<li>{line[1:].strip()}</li>")
        else:
            if in_list:
                html_lines.append('</ol>')
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append('</ol>')
    return '\n'.join(html_lines)


def parse_paragraphs(content):
    """
    Parses markdown paragraphs and converts them to HTML.
    Handles multi-line paragraphs with <br/> tags.
    """
    lines = content.split('\n')
    html_lines = []
    current_paragraph = []

    for line in lines:
        if (line.strip() and not (line.strip().startswith('<h') or
                                  line.strip().startswith('<li>') or
                                  line.strip().startswith('<ul>') or
                                  line.strip().startswith('</ul>') or
                                  line.strip().startswith('<ol>') or
                                  line.strip().startswith('</ol>'))):
            current_paragraph.append(line.strip())
        else:
            if current_paragraph:
                html_lines.append("<p>")

                for i, para_line in enumerate(current_paragraph):
                    html_lines.append(para_line)
                    if i < len(current_paragraph) - 1:
                        html_lines.append("<br/>")

                html_lines.append("</p>")
                current_paragraph = []

            if line.strip() or not current_paragraph:
                html_lines.append(line)

    if current_paragraph:
        html_lines.append("<p>")

        for i, para_line in enumerate(current_paragraph):
            html_lines.append(para_line)
            if i < len(current_paragraph) - 1:
                html_lines.append("<br/>")

        html_lines.append("</p>")

    return '\n'.join(html_lines)


def parse_bold_and_emphasis(content):
    """
    Parses markdown bold and emphasis text and converts them to HTML.
    """
    content = content.replace('**', '<strong>').replace('__', '<strong>')
    content = content.replace('*', '<em>').replace('_', '<em>')
    return content


def main():
    """
    Main function to handle markdown to HTML conversion.
    """
    content = check_args()
    html_content = parse_headings(content)
    html_content = parse_unordered_list(html_content)
    html_content = parse_ordered_list(html_content)
    html_content = parse_paragraphs(html_content)
    html_content = parse_bold_and_emphasis(html_content)
    
    output_file = sys.argv[2]
    try:
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)
    except Exception as e:
        print(f"Error writing to {output_file}: {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
