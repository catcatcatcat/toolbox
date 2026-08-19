#!/usr/bin/env python3
"""Strip the document wrapper off index.html so it can be published as an Artifact.

The Artifact host wraps the uploaded file in its own <!doctype>/<head>/<body>
skeleton, so the published file must carry only the content: <title>, the font
<link>, the <style>, and the markup. Keeping this a build step means there is
exactly one source of truth (index.html) instead of two diverging copies.

Usage: python3 build-artifact.py <output.html>
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).with_name("index.html")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2

    html = SRC.read_text(encoding="utf-8")
    start = html.index("<title>")
    end = html.index("</body>")
    body = html[start:end]
    # The </head><body> seam sits in the middle of the slice; drop just those tags.
    body = re.sub(r"</head>\s*<body[^>]*>", "\n", body, count=1)

    out = Path(sys.argv[1])
    out.write_text(body.strip() + "\n", encoding="utf-8")
    print(f"{out} <- {SRC.name} ({len(body.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
