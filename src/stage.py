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

    def time_unit_length(self) -> int:
        return max(show.time_unit_length() for show in self.shows)

    def lowest_time_unit(self) -> int:
        return min(show.start_time for show in self.shows)

    def highest_time_unit(self) -> int:
        return max(show.end_time for show in self.shows)

    def stage_name_size(self) -> int:
        return len(self.stage_name)

    def print_line(self, time_unit_length: int, time_unit_range: range) -> None:
        # print the start of the line
        print("|", end="")
        # naively print the show sections
        time_unit = time_unit_range.start
        while time_unit < time_unit_range.stop:
            shows = list(filter(lambda show: show.start_time == time_unit, self.shows))
            if shows:
                show = shows[0]
                self._print_show(time_unit_length, show)
                time_unit = show.end_time + 1
            else:
                self._print_noshow(time_unit_length)
                time_unit += 1

    def _print_show(self, time_unit_length: int, show: Show) -> None:
        show_time_units = show.end_time - show.start_time + 1
        print(f"{show.show_id:^{show_time_units*time_unit_length-1}}|", end="")

    def _print_noshow(self, time_unit_length: int) -> None:
        print(f'{" "*(time_unit_length-1)}|', end="")

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
