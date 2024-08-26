import re


class Show:
    def __init__(self, show_entry: str):
        regex = r"show_(?P<id>[0-9]*)\s+(?P<start>[0-9]*)\s+(?P<end>[0-9]*)"
        if match := re.match(regex, show_entry):
            self.show_id: str = match["id"]
            self.start_time = int(match["start"])
            self.end_time = int(match["end"])
        else:
            raise ValueError(f"invalid show entry: {show_entry.strip()}!")

    def time_unit_length(self) -> int:
        return max(self._show_time_unit_length(), self._show_id_size_for_show_time())

    def _show_time_unit_length(self) -> int:
        return max(len(str(self.start_time)) + 1, len(str(self.end_time)) + 1)

    def _show_id_size_for_show_time(self) -> int:
        # we need 1 for the trailing separator and 1 for fractions
        return int(len(self.show_id) / (self.end_time - self.start_time + 1) + 2)

    def __lt__(self, other: "Show"):
        return self.start_time < other.start_time

    def __str__(self):
        return f"show {self.show_id}: [ {self.start_time}, {self.end_time} ]"
