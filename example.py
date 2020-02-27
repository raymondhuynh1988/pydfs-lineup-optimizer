from pydfs_lineup_optimizer import Site, Sport, get_optimizer, CSVLineupExporter
from pydfs_lineup_optimizer import get_optimizer, Site, Sport
import warnings
from collections import OrderedDict
from itertools import chain
from math import ceil
from typing import FrozenSet, Type, Generator, Tuple, Union, Optional, List, Dict, Set, cast
from pydfs_lineup_optimizer.lineup import Lineup
from pydfs_lineup_optimizer.solvers import Solver, PuLPSolver, SolverException
from pydfs_lineup_optimizer.exceptions import LineupOptimizerException, LineupOptimizerIncorrectTeamName, \
    LineupOptimizerIncorrectPositionName
from pydfs_lineup_optimizer.sites import SitesRegistry
from pydfs_lineup_optimizer.lineup_importer import CSVImporter
from pydfs_lineup_optimizer.settings import BaseSettings
from pydfs_lineup_optimizer.player import Player, LineupPlayer, GameInfo
from pydfs_lineup_optimizer.utils import ratio, link_players_with_positions, process_percents, get_remaining_positions
from pydfs_lineup_optimizer.rules import *
from pydfs_lineup_optimizer.stacks import BaseGroup, TeamStack, PositionsStack, BaseStack, Stack
from collections import namedtuple
from datetime import datetime
from pytz import timezone
from typing import List, Optional
from pydfs_lineup_optimizer.utils import process_percents
from pydfs_lineup_optimizer.tz import get_timezone
import pandas as pd
import seaborn as sns
import numpy as np

optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL)
optimizer.load_players_from_csv('data/afl_data.csv')
lineup_generator = optimizer.optimize(10)
lineups = CSVLineupExporter(optimizer.optimize(n=1,randomness=True))

for lineup in lineup_generator:
    print(lineup)
