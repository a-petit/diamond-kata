class Diamond:
    def __init__(self, seed):
        self._seed = seed

    @classmethod
    def of(cls, seed):
        return Diamond(seed)

    def lines(self) -> list[str]:
        head = []
        tail = []
        for codepoint in range(ord("A"), ord(self._seed) + 1):
            line = self._line(codepoint)
            head.append(line)
            if chr(codepoint) != self._seed:
                tail.insert(0, line)
        return head + tail

    def _line(self, codepoint):
        line = self._indentation(codepoint) + chr(codepoint)
        if chr(codepoint) != "A":
            space_between = " " * ((codepoint - ord("A")) * 2 - 1)
            line += space_between + chr(codepoint)
        line += self._indentation(codepoint)
        return line

    def _indentation(self, codepoint):
        return " " * (ord(self._seed) - codepoint)


def test_a():
    assert Diamond.of("A").lines() == ["A"]


def test_top_half_contains_letter_in_ascending_order():
    lines = Diamond.of("B").lines()
    assert "A" in lines[0]
    assert "B" in lines[1]


def test_bottom_half_contains_letters_in_descending_order():
    lines = Diamond.of("B").lines()
    assert "B" in lines[1]
    assert "A" in lines[2]


def test_non_a_letters_are_doubled():
    lines = Diamond.of("C").lines()
    assert lines[1].count("B") == 2
    assert lines[2].count("C") == 2


def test_line_are_indented_in_left_angle_bracket():
    lines = Diamond.of("C").lines()
    assert lines[0].startswith("  ")
    assert lines[1].startswith(" ")
    assert lines[2].startswith("")
    assert lines[3].startswith(" ")
    assert lines[4].startswith("  ")


def test_line_are_suffix_indented_in_right_angle_bracket():
    lines = Diamond.of("C").lines()
    assert lines[0].endswith("  ")
    assert lines[1].endswith(" ")
    assert lines[2].endswith("")
    assert lines[3].endswith(" ")
    assert lines[4].endswith("  ")


def test_letters_are_spaced():
    lines = Diamond.of("C").lines()
    assert lines[0].strip() == "A"
    assert lines[1].strip() == "B B"
    assert lines[2].strip() == "C   C"
    assert lines[3].strip() == "B B"
    assert lines[4].strip() == "A"


def test_b():
    assert Diamond.of("B").lines() == [
        " A ",
        "B B",
        " A ",
    ]


def test_c():
    assert Diamond.of("C").lines() == [
        "  A  ",
        " B B ",
        "C   C",
        " B B ",
        "  A  ",
    ]