#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from engine import Engine
from input_handlers import EventHandler

def main() -> None:
  screen_width = 80
  screen_height = 50

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

  npc = Entity(
    int(screen_width / 2) - 5,
    int(screen_height / 2),
    "@",
    (255, 255, 0)
  )

  entities = { player, npc }

  game = Engine(entities, event_handler, player)

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