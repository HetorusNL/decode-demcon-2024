from src.show import Show


class Stage:
    def __init__(self, stage_name: str):
        self.stage_name = stage_name
        self.shows: list[Show] = []

    def add_show(self, show: Show) -> bool:
        """tries to add the show at the stage

        returns:
        - true when the show is added to the schedule of the stage
        - false when it doesn't fit the schedule of the stage
        """
        if self._overlaps(show):
            # it intersects with at least one show, it doesn't fit
            return False

        # otherwise it fits, add the show and return
        self.shows.append(show)
        return True

    def _overlaps(self, show: Show) -> bool:
        for stage_show in self.shows:
            # check if show is fully before stage_show
            if show.end_time < stage_show.start_time:
                continue
            # check if show is fully after stage_show
            if show.start_time > stage_show.end_time:
                continue
            # otherwise the show overlaps, so we can't add it here
            return True
        # if we get here, there is no overlapping show
        return False

    def __str__(self):
        print_info: str = f"{self.stage_name}:\n"
        print_info += "\n".join([f" * {str(show)}" for show in sorted(self.shows)])
        return print_info
