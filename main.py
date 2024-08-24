import sys

from src.demcon_festival_planner import DemconFestivalPlanner

# if a filename has been provided, use that
# otherwise use the default file in DemconFestivalPlanner
if len(sys.argv) > 1:
    DemconFestivalPlanner(sys.argv[1])
else:
    DemconFestivalPlanner()
