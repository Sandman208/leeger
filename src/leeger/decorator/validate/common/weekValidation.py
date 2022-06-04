from src.leeger.decorator.validate.common import matchupValidation
from src.leeger.exception.InvalidWeekFormatException import InvalidWeekFormatException
from src.leeger.model.Week import Week


def checkAllTypes(week: Week) -> None:
    """
    Checks all types that are within the Week object.
    """

    if type(week.weekNumber) != int:
        raise InvalidWeekFormatException("Week number must be type 'int'.")
    if type(week.isPlayoffWeek) != bool:
        raise InvalidWeekFormatException("Week isPlayoffWeek must be type 'bool'.")
    if type(week.isChampionshipWeek) != bool:
        raise InvalidWeekFormatException("Week isChampionshipWeek must be type 'bool'.")
    if type(week.matchups) != list:
        raise InvalidWeekFormatException("Week matchups must be type 'list'.")

    for matchup in week.matchups:
        matchupValidation.checkAllTypes(matchup)


def checkWeekHasAtLeastOneMatchup(week: Week) -> None:
    """
    Checks that the given Week has at least one matchup.
    """
    if len(week.matchups) == 0:
        raise InvalidWeekFormatException(f"Week {week.weekNumber} must have at least 1 matchup.")
