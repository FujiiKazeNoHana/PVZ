import sys
import pygame

from src.config import (
	WINDOW_WIDTH,
	WINDOW_HEIGHT,
	WINDOW_TITLE,
	FPS,
	COLOR_BG,
	COLOR_TEXT,
)
from src.levels.grid import Grid
from src.entities.plant import Plant
from src.entities.zombie import Zombie
from src.entities.projectile import Projectile


class Game:
	def __init__(self) -> None:
		pygame.init()
		self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption(WINDOW_TITLE)
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont("consolas", 18)

		self.grid = Grid()

		# 占位演示：放一个植物、一个僵尸和一枚子弹
		cell_center = self.grid.get_cell_center(row=2, col=2)
		self.plants = [Plant(position=cell_center)]
		self.zombies = [Zombie(position=(WINDOW_WIDTH - 80, cell_center[1]))]
		self.projectiles = [Projectile(position=(cell_center[0] + 20, cell_center[1]))]

		self.running = True

	def run(self) -> None:
		while self.running:
			self._handle_events()
			self._update()
			self._render()
			self.clock.tick(FPS)

		self._shutdown()

	def _handle_events(self) -> None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.running = False

	def _update(self) -> None:
		# 更新占位实体
		for projectile in self.projectiles:
			projectile.update()

		for zombie in self.zombies:
			zombie.update()

		# 简单的屏幕外回收
		self.projectiles = [p for p in self.projectiles if p.is_on_screen()]

	def _render(self) -> None:
		self.screen.fill(COLOR_BG)

		# 网格
		self.grid.draw(self.screen)

		# 实体
		for plant in self.plants:
			plant.draw(self.screen)

		for zombie in self.zombies:
			zombie.draw(self.screen)

		for projectile in self.projectiles:
			projectile.draw(self.screen)

		# 文本 HUD
		fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, COLOR_TEXT)
		self.screen.blit(fps_text, (10, 10))

		pygame.display.flip()

	def _shutdown(self) -> None:
		pygame.quit()
		sys.exit(0)


