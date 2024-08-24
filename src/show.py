import re


class Show:
    def __init__(self, show_entry: str):
        regex = r"show_(?P<id>[0-9]*)\s+(?P<start>[0-9]*)\s+(?P<end>[0-9]*)"
        if match := re.match(regex, show_entry):
            self.show_id = match["id"]
            self.start_time = int(match["start"])
            self.end_time = int(match["end"])
        else:
            raise ValueError(f"invalid show entry: {show_entry.strip()}!")

    def __lt__(self, other: "Show"):
        return self.start_time < other.start_time

    def __str__(self):
        return f"show {self.show_id}: [ {self.start_time}, {self.end_time} ]"
