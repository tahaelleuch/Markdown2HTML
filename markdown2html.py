#!/usr/bin/python3
"""Markdown"""

import os
import sys

if __name__ == "__main__":
    """markdown"""
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    exit(0)