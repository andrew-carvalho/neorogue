#!/usr/bin/env python3
import copy

import tcod

import colors

from engine import Engine
import entities_list
from procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_enemies_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entities_list.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms,
        room_min_size,
        room_max_size,
        map_width,
        map_height,
        max_enemies_per_room,
        engine,
    )

    engine.update_fov()

    engine.log.add_message(
        "Hello Rogue and welcome to yet another dungeon!", colors.welcome_text
    )

    with tcod.context.new_terminal(
        screen_width, screen_height, tileset=tileset, title="Neorogue", vsync=True
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")

        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            engine.event_handler.handle_events(context)


if __name__ == "__main__":
    main()
