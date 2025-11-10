import pygame

from src.config import (
	GRID_ROWS,
	GRID_COLS,
	CELL_WIDTH,
	CELL_HEIGHT,
	GRID_OFFSET_X,
	GRID_OFFSET_Y,
	COLOR_GRID,
	COLOR_GRID_ALT,
)


class Grid:
	def __init__(self) -> None:
		self.rows = GRID_ROWS
		self.cols = GRID_COLS

	def get_cell_rect(self, row: int, col: int) -> pygame.Rect:
		x = GRID_OFFSET_X + col * CELL_WIDTH
		y = GRID_OFFSET_Y + row * CELL_HEIGHT
		return pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)

	def get_cell_center(self, row: int, col: int) -> tuple[int, int]:
		rect = self.get_cell_rect(row, col)
		return rect.centerx, rect.centery

	def draw(self, surface: pygame.Surface) -> None:
		for r in range(self.rows):
			for c in range(self.cols):
				rect = self.get_cell_rect(r, c)
				color = COLOR_GRID_ALT if (r + c) % 2 else COLOR_GRID
				pygame.draw.rect(surface, color, rect, border_radius=6)
				pygame.draw.rect(surface, (0, 0, 0), rect, width=1, border_radius=6)


