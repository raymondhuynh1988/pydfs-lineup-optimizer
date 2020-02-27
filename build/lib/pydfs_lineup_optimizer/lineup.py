from typing import List, Type
from pydfs_lineup_optimizer.player import LineupPlayer
from pydfs_lineup_optimizer.lineup_printer import BaseLineupPrinter, LineupPrinter


class Lineup:
    def __init__(self, players: List[LineupPlayer], printer: Type[BaseLineupPrinter] = LineupPrinter):
        self.players = players
        self.printer = printer()

    def __iter__(self):
        return iter(self.players)

    def __contains__(self, item):
        return item in self.players

    def __str__(self):
        return self.printer.print_lineup(self)

    def __repr__(self):
        return 'Lineup: projection %s, budget %s' % (self.fantasy_points_projection, self.salary_costs)

    def __hash__(self):
        return hash(sorted(p.id for p in self))

    def __eq__(self, other):
        return hash(self) == hash(other)

    @property
    def lineup(self) -> List[LineupPlayer]:
        return self.players

    @property
    def fantasy_points_projection(self) -> float:
        return round(sum(player.fppg for player in self.players), 3)

    @property
    def salary_costs(self) -> int:
        return sum(player.salary for player in self.players)

    def get_unswappable_players(self) -> List[LineupPlayer]:
        return [player for player in self.players if player.is_game_started]
