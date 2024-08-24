from src.show import Show
from src.stage import Stage


class Stages:
    def __init__(self):
        self.stages: list[Stage] = []

    def add_show(self, show: Show):
        """add a show to first available stage where the it doesn't overlap"""
        # loop through all currently available stages
        for stage in self.stages:
            # try to schedule a show at the current stage
            if stage.add_show(show):
                return
        # if we get here, there is no stage yet to schedule the show
        # create a new one and add the show there
        # let's think of an original stage name: 'stage' with an identifier :)
        # just like the shows, let's start counting at '1'
        stage_name: str = f"stage {len(self.stages)+1}"
        stage = Stage(stage_name)
        stage.add_show(show)
        self.stages.append(stage)

    def __str__(self):
        return "\n".join([str(stage) for stage in self.stages])
