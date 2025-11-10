## 植物大战僵尸（简版）- Python + Pygame

一个用于起步的项目骨架，包含最小可运行的 Pygame 主循环、占位实体与网格绘制。

### 运行环境（Windows PowerShell）

1) 创建并激活虚拟环境（建议）

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

若执行策略阻止激活，可临时放宽（管理员 PowerShell）后再尝试：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

2) 安装依赖

```powershell
pip install -r requirements.txt
```

3) 运行游戏

```powershell
python -m src.main
```

### 目录结构

```
PVZ/
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ src/
   ├─ __init__.py
   ├─ main.py
   ├─ config.py
   ├─ core/
   │  ├─ __init__.py
   │  └─ game.py
   ├─ entities/
   │  ├─ __init__.py
   │  ├─ plant.py
   │  ├─ zombie.py
   │  └─ projectile.py
   └─ levels/
      ├─ __init__.py
      └─ grid.py
```

### 下一步可做

- 增加碰撞检测与简单 AI
- 关卡与波次生成
- 资源加载（图片/音效）与动画
- UI（开始菜单、暂停、分数/阳光等）

### 使用 Git 与协作（示例流程）

1) 初始化本地仓库并首推

```powershell
git init
git add .
git commit -m "init: pygame PVZ starter"
git branch -M main
git remote add origin <你的远程仓库URL>  # 例如：https://github.com/<user>/PVZ.git
git push -u origin main
```

2) 团队协作分支模型（推荐）
- 主分支：`main`（受保护，不直接提交）
- 功能分支：从 `main` 切出，如 `feature/grid-collision`

```powershell
git checkout -b feature/<短描述>
# ... 开发、提交 ...
git push -u origin feature/<短描述>
```

3) 提交与代码评审
- 在 GitHub/GitLab 开 Pull Request（PR）到 `main`
- 通过代码评审后合并；开启“禁止直接推送 main、要求至少 1 评审”的保护规则

4) 同步最新代码
```powershell
git checkout main
git pull --ff-only origin main
git checkout feature/<短描述>
git rebase main   # 或 git merge main
```

5) Windows 上的换行与编码
- 已提供 `.gitattributes` 与 `.editorconfig`，建议执行：
```powershell
git config --global core.autocrlf true
```
这会在 Windows 工作站上检出为 CRLF、提交时规范为 LF（仓库保持一致）。

6) 忽略文件
- `.gitignore` 已包含常见 Python/IDE/虚拟环境忽略项，提交前确保 `.venv/` 未被纳入版本控制。

7) 协作注意事项
- 每个功能原子提交，提交信息使用动词前缀：feat/fix/refactor/docs/chore
- 对于依赖变更：更新 `requirements.txt`，并在 PR 描述标注“需要重新安装依赖”
- 二进制资源较大时建议使用 Git LFS 或发布到独立存储


