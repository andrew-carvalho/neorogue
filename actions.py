from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()


class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()


class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()


class MeleeAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        target = engine.game_map.get_blocking_entity(dest_x, dest_y)
        if not target:
            return

        print(f"Atack {target.name}!")


class MovementAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return

        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return

        if engine.game_map.get_blocking_entity(dest_x, dest_y):
            return

        entity.move(self.dx, self.dy)


class BumpAction(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity(dest_x, dest_y):
            MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            MovementAction(self.dx, self.dy).perform(engine, entity)
