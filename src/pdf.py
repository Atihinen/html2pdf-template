import argparse
from pathlib import Path
import pdfkit

STATIC = Path("static")
CSS = STATIC / "default.css"

OPTIONS = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None
}

def create_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--value", help="Value for the template",
                    default="Testing")
    return parser

def _get_template():
    with open(STATIC / "template.html", "r") as f:
        template = f.read()
    return template
    
def render(value):
    template = _get_template()
    pdfkit.from_string(template.format(value=value), 'out.pdf', options=OPTIONS, css=CSS)

def main():
    parser = create_argparse()
    args = parser.parse_args()
    render(args.value)


if __name__ == "__main__":
    main()

