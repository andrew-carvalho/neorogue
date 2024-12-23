from __future__ import annotations

from typing import TYPE_CHECKING

import colors

from entity import Actor

if TYPE_CHECKING:
    from tcod import Console


def render_ui(console: Console, player: Actor):
    console.print(
        x=1,
        y=46,
        string=f"HP:  {player.fighter.hp}\{player.fighter.max_hp}",
    )

    console.print(
        x=1,
        y=47,
        string=f"DEF: {player.fighter.power}",
    )

    console.print(
        x=1,
        y=48,
        string=f"POW: {player.fighter.power}",
    )
