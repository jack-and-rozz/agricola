import abc
import itertools
from future.utils import with_metaclass
from .choice import (ActionChoice)
from . import const

class Step(with_metaclass(abc.ABCMeta, object)):
    def __init__(self, game, player):
        self.game = game
        self.player = player

    @property
    def required_choice(self):
        return None, None

    # returns next stack items
    def effect(self, choice):
        return None

class ActionStep(Step):
    @property
    def required_choice_and_source(self):
        return ActionChoice, const.event_sources.game

    def effect(self, choise):
        self.game.actions_taken[choise.choice_value] = self.player.index
        self.game.actions_remaining.remove(choise.choice_value)
        self.game.players[self.player.index].turn_left -= 1
        return choise.choice_value.effect(self.player)
        
