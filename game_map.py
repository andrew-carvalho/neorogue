from __future__ import annotations

from typing import Iterable, Optional, TYPE_CHECKING

import numpy as np
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity


class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width = width
        self.height = height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")
        self.visible = np.full((width, height), fill_value=False, order="F")
        self.explored = np.full((width, height), fill_value=False, order="F")

    def get_blocking_entity(self, x: int, y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.block_movement and entity.x == x and entity.y == y:
                return entity
        return None

    def in_bounds(self, x: int, y: int):
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console):
        console.rgb[0 : self.width, 0 : self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.UNEXPLORED,
        )

        for entitiy in self.entities:
            if self.visible[entitiy.x, entitiy.y]:
                console.print(
                    x=entitiy.x, y=entitiy.y, string=entitiy.char, fg=entitiy.color
                )
