import sys
import random
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

		# 占位演示：放一个僵尸和一枚子弹（初始不放植物以便点击放置）
		center_row, center_col = 2, 2
		cell_center = self.grid.get_cell_center(row=center_row, col=center_col)
		self.plants: list[Plant] = []
		self.zombies = [Zombie(position=(WINDOW_WIDTH - 80, cell_center[1]))]
		self.projectiles = [Projectile(position=(cell_center[0] + 20, cell_center[1]))]
		# 跟踪已占用的网格（避免重复放置同一格）
		self.occupied_cells: set[tuple[int, int]] = set()

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
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				self._try_place_plant_at_mouse()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
				self._spawn_zombie_at_mouse_row()

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

	def _try_place_plant_at_mouse(self) -> None:
		pos = pygame.mouse.get_pos()
		cell = self.grid.get_cell_at_pos(pos)
		if cell is None:
			return
		row, col = cell
		if (row, col) in self.occupied_cells:
			return
		center = self.grid.get_cell_center(row, col)
		plant = Plant(position=center, row=row, col=col)
		self.plants.append(plant)
		self.occupied_cells.add((row, col))

	def _spawn_zombie_random_row(self) -> None:
		# 在随机行的右侧边缘外一些生成一个僵尸，并向左移动
		row = random.randint(0, self.grid.rows - 1)
		_, y = self.grid.get_cell_center(row, 0)
		spawn_x = WINDOW_WIDTH - 40
		self.zombies.append(Zombie(position=(spawn_x, y)))  # 默认速度为负，向左移动

	def _spawn_zombie_at_mouse_row(self) -> None:
		px, py = pygame.mouse.get_pos()
		row = self.grid.get_row_by_y(py)
		if row is None:
			return
		_, y = self.grid.get_cell_center(row, 0)
		spawn_x = WINDOW_WIDTH - 40
		self.zombies.append(Zombie(position=(spawn_x, y)))  # 默认向左移动


