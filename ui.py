from __future__ import annotations

from typing import TYPE_CHECKING

from entity import Actor

import colors

if TYPE_CHECKING:
    from tcod.console import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_position(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ",".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()


def render_ui(console: Console, player: Actor):
    console.print(
        x=1,
        y=44,
        string=f"HP:  {player.fighter.hp}/{player.fighter.max_hp}",
    )

    console.print(
        x=1,
        y=45,
        string=f"DEF: {player.fighter.power}",
    )

    console.print(
        x=1,
        y=46,
        string=f"POW: {player.fighter.power}",
    )


def render_names_at_mouse_position(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_position

    names_at_mouse_position = get_names_at_position(mouse_x, mouse_y, engine.game_map)

    console.print(x=x, y=y, string=names_at_mouse_position, fg=colors.pointing_at_log)
