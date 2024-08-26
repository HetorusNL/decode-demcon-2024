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

    def fancy_print(self):
        # time unit length is the max value of:
        # - the len() of the time unit str itself
        # - the len() of the show id divided by the num of time units
        time_unit_length = max(stage.time_unit_length() for stage in self.stages)
        time_unit_length += 1  # some more space
        lowest_time_unit = min(stage.lowest_time_unit() for stage in self.stages)
        highest_time_unit = max(stage.highest_time_unit() for stage in self.stages)
        time_unit_range = range(lowest_time_unit, highest_time_unit + 1)
        stage_size = 2 + max(stage.stage_name_size() for stage in self.stages)

        # construct all basic ascii art lines
        stage_name_empty = f'{stage_size*" "}'
        stage_name_full = f'{stage_size*"-"}'
        stage_height = 10
        offset = (stage_height + 1) * " "
        outer_length = (time_unit_range.stop - 1) * time_unit_length + 1
        inner_length = (time_unit_range.stop - 1) * time_unit_length - 1
        inner_time_unit = time_unit_length - 1
        top_row = offset + f'|-{stage_name_full}-{outer_length*"-"}--|'
        empty_row = offset + f'| {stage_name_empty} {outer_length*" "}  |'
        time_border_row = offset + f'| {stage_name_empty} |{inner_length*"-"}|  |'
        filled_cell = f'{inner_time_unit*"-"+"|"}'
        filled_separator_row = (
            offset + f"| {stage_name_empty} |{(time_unit_range.stop-1)*filled_cell}  |"
        )

        # fill the top portion of the ascii art stage
        print(top_row)
        print(empty_row)
        print(time_border_row)
        # add an time unit row
        print(offset + f"| {stage_name_empty} |", end="")
        for time_unit in time_unit_range:
            print(f"{time_unit:^{inner_time_unit}}|", end="")
        print("  |")
        # add the shows separated by a separator row
        for stage in self.stages:
            print(filled_separator_row)
            print(f"{offset}|  {stage.stage_name:<{stage_size-1}} ", end="")
            stage.print_line(time_unit_length, time_unit_range)
            print("  |")
        # end with the bottom portion of the ascii art stage pack plane
        print(time_border_row)
        print(empty_row)
        print(top_row)

        # add a fancy 3D stage
        stage_row_size = outer_length + 2 * stage_height + 2
        full_stage_row = f'|-{stage_name_full}-{stage_row_size*"-"}--|'
        empty_stage_row = f'| {stage_name_empty} {stage_row_size*" "}  |'
        for i in range(stage_height):
            print(f'{(stage_height-i)*" "}/{i*" "}', end="")
            center = (time_unit_range.stop - 1) * time_unit_length + 2 + stage_size
            print(f'  {center*" "}   ', end="")
            print(f'{i*" "}\\')
        print(full_stage_row)
        print(empty_stage_row)
        print(empty_stage_row)
        print(empty_stage_row)
        print(full_stage_row)

    def __str__(self):
        return "\n".join([str(stage) for stage in self.stages])
