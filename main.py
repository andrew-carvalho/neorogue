#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
  screen_width = 80
  screen_height = 50

  map_width = 80
  map_height = 45

  room_max_size = 10
  room_min_size = 6
  max_rooms = 30

  tileset = tcod.tileset.load_tilesheet(
    "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
  )

  event_handler = EventHandler()

  player = Entity(
    int(screen_width / 2),
    int(screen_height / 2),
    "@",
    (255, 255, 255)
  )

  entities = { player }

  game_map = generate_dungeon(
    max_rooms,
    room_min_size,
    room_max_size,
    map_width,
    map_height,
    player
  )

  game = Engine(entities, event_handler, game_map, player)

  with tcod.context.new_terminal(
    screen_width,
    screen_height,
    tileset=tileset,
    title="Neorogue",
    vsync=True
  ) as context:
    root_console = tcod.console.Console(screen_width, screen_height, order="F")

    while True:
      game.render(root_console, context)
      events = tcod.event.wait()
      game.handle_events(events)

if __name__ == "__main__":
  main()