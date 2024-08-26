from pathlib import Path

from src.show import Show
from src.stages import Stages


class DemconFestivalPlanner:
    def __init__(self, input_file: str = "input.txt"):
        self.input_file: Path = Path(input_file)
        self.parse_input()

    def parse_input(self):
        with open(self.input_file) as f:
            lines = f.readlines()

        # create a collection of Stage objects to store our shows in
        stages = Stages()
        shows = [Show(line) for line in lines]
        for show in sorted(shows):
            stages.add_show(show)

        # show the stages and their shows as a list
        print(stages)

        # print a fancy ascii art stage with show timelines
        stages.fancy_print()
