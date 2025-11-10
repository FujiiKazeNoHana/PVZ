import pygame

from src.config import COLOR_PLANT


class Plant:
	def __init__(self, position: tuple[int, int]) -> None:
		self.position = position
		self.radius = 22

	def draw(self, surface: pygame.Surface) -> None:
		pygame.draw.circle(surface, COLOR_PLANT, self.position, self.radius)


