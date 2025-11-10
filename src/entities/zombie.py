import pygame

from src.config import COLOR_ZOMBIE


class Zombie:
	def __init__(self, position: tuple[int, int], speed: float | None = None) -> None:
		self.x = float(position[0])
		self.y = float(position[1])
		self.width = 36
		self.height = 48
		# 默认从右向左移动（负方向），以兼容原始生成点在右侧的逻辑
		self.speed = -0.3 if speed is None else float(speed)

	def update(self) -> None:
		# speed > 0 向右，speed < 0 向左
		self.x += self.speed

	def draw(self, surface: pygame.Surface) -> None:
		rect = pygame.Rect(int(self.x - self.width / 2), int(self.y - self.height / 2), self.width, self.height)
		pygame.draw.rect(surface, COLOR_ZOMBIE, rect, border_radius=6)


