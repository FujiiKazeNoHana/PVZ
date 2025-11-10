import pygame

from src.config import COLOR_PROJECTILE, WINDOW_WIDTH


class Projectile:
	def __init__(self, position: tuple[int, int]) -> None:
		self.x = float(position[0])
		self.y = float(position[1])
		self.radius = 6
		self.speed = 3.0

	def update(self) -> None:
		self.x += self.speed

	def is_on_screen(self) -> bool:
		return 0 <= self.x <= WINDOW_WIDTH + 50

	def draw(self, surface: pygame.Surface) -> None:
		pygame.draw.circle(surface, COLOR_PROJECTILE, (int(self.x), int(self.y)), self.radius)


