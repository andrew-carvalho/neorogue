from typing import Tuple

import numpy as np

graphics_dt = np.dtype(
  [
    ("ch", np.int32),
    ("fg", "3B"), # 3 unsigned bytes
    ("bg", "3B") 
  ]
)

tile_dt = np.dtype(
  [
    ("walkable", np.bool),
    ("transparent", np.bool), # Block FOV
    ("dark", graphics_dt) # Graphics for when tile is not in FOV
  ]
)

def new_tile(
    *, # Parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]
  ) -> np.ndarray:
  return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
  walkable=True,
  transparent=True,
  dark=(ord(" "), (255,255,255), (50,50,150))
)

wall = new_tile(
  walkable=False,
  transparent=False,
  dark=(ord(" "), (255,255,255), (0,0,100))
)