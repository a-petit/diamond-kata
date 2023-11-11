class Diamond:
    def __init__(self, seed):
        self._seed = seed

    @classmethod
    def of(cls, seed) -> 'Diamond':
        return Diamond(seed)

    def representation(self) -> str:
        head = ""
        tail = ""
        for codepoint in range(ord("A"), ord(self._seed) + 1):
            line = self._line(codepoint)
            head += line
            if chr(codepoint) != self._seed:
                tail = line + tail
        return head + tail

    def _line(self, codepoint):
        line = ""
        line += self._indentation(codepoint)
        line += chr(codepoint)
        if chr(codepoint) != "A":
            space_between = " " * ((codepoint - ord("A")) * 2 - 1)
            line += space_between + chr(codepoint)
        line += self._indentation(codepoint)
        line += "\n"
        return line

    def _indentation(self, codepoint):
        return " " * (ord(self._seed) - codepoint)


def test_a():
    assert Diamond.of("A").representation() == "A\n"


def test_b():
    assert Diamond.of("B").representation() == "" + \
           " A \n" + \
           "B B\n" + \
           " A \n"


def test_c():
    assert Diamond.of("C").representation() == "" + \
        "  A  \n" + \
        " B B \n" + \
        "C   C\n" + \
        " B B \n" + \
        "  A  \n"
