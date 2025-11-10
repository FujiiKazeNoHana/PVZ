import pygame

from src.config import COLOR_ZOMBIE


class Zombie:
	def __init__(self, position: tuple[int, int]) -> None:
		self.x = float(position[0])
		self.y = float(position[1])
		self.width = 36
		self.height = 48
		self.speed = 0.3  # 占位缓慢移动

	def update(self) -> None:
		self.x -= self.speed

	def draw(self, surface: pygame.Surface) -> None:
		rect = pygame.Rect(int(self.x - self.width / 2), int(self.y - self.height / 2), self.width, self.height)
		pygame.draw.rect(surface, COLOR_ZOMBIE, rect, border_radius=6)


