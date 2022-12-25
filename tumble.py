# Utilities for printing tabular data
import sys
from typing import TextIO, Tuple


class Tumble:
    def __init__(self, *columns: Tuple[str, int, str], printHeader=True, stream: TextIO = None, align: str = '^') -> None:
        """
        Create a new table to format

        columns: list of tuples (column name: str, max width, format type)
        """

        self._format_str = ''
        self._header = ''
        self._stream: TextIO = stream if stream is not None else sys.stdout

        # Init lists
        header_vals = [""] * len(columns)
        format_vals = [0] * len(columns)
        line_vals = [""] * len(columns)

        for idx, (name, width, fmt) in enumerate(columns):
            name = str(name).strip()
            width = max(int(width), len(name))
            fmt = str(fmt)

            name_fmt = f'| {{:{align}{width}s}} '
            header_vals[idx] = name_fmt.format(name)
            format_vals[idx] = f'| {{:{align}{width}{fmt}}} '
            line_vals[idx] = f'|{"-" * (len(header_vals[idx]) - 1)}'

        self._header = "".join(header_vals) + "|\n" + "".join(line_vals) + "|"
        self._format_str = "".join(format_vals).strip() + " |"

        del header_vals
        del format_vals

        if printHeader:
            self.print_header()

    def print_header(self) -> None:
        print(self._header, file=self._stream)

    def header(self) -> str:
        return self._header

    def row(self, *values) -> str:
        return self._format_str.format(*values)

    def print_row(self, *values) -> None:
        print(self.row(*values), file=self._stream)
