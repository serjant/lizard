''' extensions of lizard '''

from __future__ import print_function
from .htmloutput import html_output
from .xmloutput import xml_output


def print_xml(results, options):
    print(xml_output(list(results), options.verbose))
