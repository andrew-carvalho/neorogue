from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from input_handlers import GameOverEventHandler
from render_order import RenderOrder

import colors

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    entity: Actor

    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.entity.ai:
            self.die()

    def die(self) -> None:
        if self.engine.player is self.entity:
            death_message = "You Died! Game over."
            death_message_color = colors.player_die_log
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message_color = colors.enemy_die_log
            death_message = f"{self.entity.name} is dead!"

        self.entity.char = "%"
        self.entity.color = (191, 0, 0)
        self.entity.block_movement = False
        self.entity.ai = None
        self.entity.name = f"Remains of {self.entity.name}"
        self.entity.render_order = RenderOrder.CORPSE

        self.engine.log.add_message(death_message, death_message_color)
