# DataFinderAgentOS 部署文档

## 系统概述
- **系统名称**：某政务智能瞭望与智能问数系统（DataFinderAgentOS）
- **系统类型**：Web B/S 结构的数据智能采集和数据智能问数系统
- **技术栈**：Python 3.10+ / Tornado 6.x / SQLite / Layui 2.9.x / Bootstrap 5.3.8

---

## 一、环境要求

| 项目 | 要求 |
|------|------|
| Python | 3.10 及以上版本（推荐 3.13） |
| 操作系统 | Windows / Linux / macOS（跨平台） |
| 磁盘空间 | 至少 500MB（含依赖和数据库） |
| 内存 | 至少 512MB |
| 网络 | 需要访问 OpenAI 兼容 API（模型对话功能） |
| 浏览器 | Chrome / Edge / Firefox 最新版 |

---

## 二、依赖安装

### 2.1 核心依赖
```bash
pip install tornado>=6.0
```

### 2.2 深度采集依赖（可选，深度采集功能需要）
```bash
pip install crawl4ai>=0.9.1
```
> crawl4ai 基于 Playwright，首次使用需要额外安装浏览器：
```bash
playwright install chromium
```

### 2.3 requirements.txt（一键安装）
项目目录下创建 `requirements.txt` 文件，内容如下：
```
tornado>=6.0
crawl4ai>=0.9.1
```
一键安装命令：
```bash
pip install -r requirements.txt
```

---

## 三、项目部署步骤

### 3.1 克隆仓库
```bash
git clone https://github.com/Sophia-star11/DataFinderAgentOS-group.git
cd DataFinderAgentOS-group
```

### 3.2 创建虚拟环境
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3.3 安装依赖
```bash
pip install -r requirements.txt
```

### 3.4 启动服务
```bash
python run.py
```

启动成功后终端输出：
```
Server Started:http://localhost:10010/
```

### 3.5 访问系统
| 入口 | 地址 | 说明 |
|------|------|------|
| 管理侧后台 | http://localhost:10010/admin/ | 管理员登录 |
| 用户侧前台 | http://localhost:10010/ | 用户登录/注册 |

---

## 四、默认账号

| 用户名 | 密码 | 角色 | 说明 |
|--------|------|------|------|
| admin | 123456 | 超级管理员 | 系统预置，不可删除 |
| （自行注册） | （自行设置） | 普通用户 | 用户侧注册后自动分配 |

---

## 五、数据库说明

- **类型**：SQLite 单文件数据库
- **路径**：`database/finderos.db`
- **创建方式**：首次启动 `run.py` 时自动创建并初始化表结构
- **数据迁移**：数据库自动完成表结构创建和初始数据填充，无需手动操作

### 数据库核心表
| 表名 | 说明 |
|------|------|
| `users` | 用户表 |
| `roles` | 角色表 |
| `functions` | 功能表（系统菜单功能定义） |
| `menus` | 菜单表（按角色配置的菜单） |
| `role_functions` | 角色-功能关联表 |
| `watch_sources` | 瞭源配置表 |
| `watch_collected_data` | 瞭望采集数据表 |
| `data_warehouse` | 数据仓库表 |
| `deep_collect_tasks` | 深度采集任务表 |
| `deep_collect_data` | 深度采集结果表 |
| `ai_models` | 模型引擎配置表 |
| `digital_employees` | 数字员工表 |
| `conversations` | 对话历史表 |

---

## 六、配置说明

当前版本的配置（端口、密钥等）直接在 `run.py` 中配置，后续版本将迁移到 `config/` 目录。

### 当前可调整的配置项（修改 `run.py`）

| 配置项 | 位置（行号） | 默认值 | 说明 |
|--------|------------|--------|------|
| 服务端口 | `run.py:651` | `10010` | `server.listen(10010)` |
| Cookie 密钥 | `run.py:118` | `datafinderagentos-token` | 用于会话加密 |
| XSRF 防护 | `run.py:120` | `True` | 跨站请求伪造防护 |

### AI 模型配置
模型对话通过模型引擎页面在后台配置，支持任何 OpenAI 兼容 API：
- API Base URL
- API Key
- 模型名称（如 qwen3.5-plus、agnes-2.0-flash 等）

---

## 七、功能模块清单

### 管理侧（后台 /admin/）
| 模块 | 路由 | 说明 |
|------|------|------|
| 控制台 | /admin/ | 首页仪表盘，实时统计 |
| 用户管理 | /admin/user-management | 用户 CRUD、超管保护 |
| 角色管理 | /admin/role-management | 角色 CRUD、功能分配树、编辑弹窗 |
| 功能管理 | /admin/function-management | 功能 CRUD、父子层级 |
| 菜单管理 | /admin/menu-management | 菜单 CRUD、排序、预览 |
| 瞭源管理 | /admin/source-management | 采集源 CRUD、URL 模板配置 |
| 瞭望采集 | /admin/watch-management | 采集执行、橱窗展示 |
| 数据仓库 | /admin/warehouse-management | 数据列表、深度采集、批量操作 |
| 模型引擎 | /admin/model-engine | 模型 CRUD、SSE 对话测试 |
| 数字员工 | /admin/digital-employee | 员工 CRUD、LLM/API 双型 |
| 个人信息 | （弹窗） | 查看信息、修改密码 |

### 用户侧（前台 /）
| 模块 | 路由 | 说明 |
|------|------|------|
| 登录 | /login | 双栏品牌布局 |
| 注册 | /register | 含表单验证 |
| 对话 | /chat | 五区 ChatGPT 布局、SSE 流式 |
| @技能命令 | /chat（集成） | @天气/@新闻/@音乐/@电影/@yummy |
| /快捷功能 | /chat（集成） | 生成报表/图表/数据分析/导出报告 |

---

## 八、项目目录结构

```
DataFinderAgentOS-group/
├── run.py                          # 项目入口
├── app/
│   ├── controllers/                # 控制层（16个模块）
│   ├── models/                     # 模型层（13个模块）
│   ├── static/                     # 静态资源（CSS/JS/第三方库）
│   └── templates/                  # 模板目录
│       ├── *.html                  # 用户侧页面（5个）
│       └── admin/*.html            # 后台管理侧页面（13个）
├── config/                         # 配置目录（预留）
├── database/                       # 数据库目录
│   └── finderos.db                 # SQLite 数据库
├── data/                           # 数据存储目录
│   └── dgUser/                     # 数字员工 MD 文件
├── docs/                           # 开发文档
├── skills/                         # 技能目录（预留）
├── test/                           # 测试代码
├── venv/                           # Python 虚拟环境
└── .gitignore
```

---

## 九、常见问题

### Q1: 启动后访问 http://localhost:10010/admin/ 只显示"数据仓库"菜单
**原因**：数据库已存在但菜单数据不完整。
**解决**：删除 `database/finderos.db` 后重新启动 `run.py`，系统会自动重建完整菜单。

### Q2: 对话功能报错 403
**原因**：XSRF token 缺失。
**解决**：确保前端请求包含 XSRF token，Tornado 的 XSRF 防护已正确配置。

### Q3: crawl4ai 深度采集功能不可用
**原因**：未安装 crawl4ai 或 Playwright 浏览器。
**解决**：
```bash
pip install crawl4ai>=0.9.1
playwright install chromium
```

### Q4: 模型对话无响应
**原因**：模型引擎未配置有效的 API 密钥和地址。
**解决**：登录后台 → 模型引擎 → 新增/编辑模型 → 填写正确的 API Base URL 和 API Key。

### Q5: 组员拉取代码后菜单不完整
**原因**：`run.py` 初始化逻辑已包含通用菜单保障循环，会自动补全。
**解决**：直接启动 `run.py` 即可，无需手动操作数据库。

---

## 十、Git 仓库信息

| 项目 | 内容 |
|------|------|
| 团队仓库 | https://github.com/Sophia-star11/DataFinderAgentOS-group |
| 个人仓库 | https://github.com/Sophia-star11/DataFinderAgentOSv1 |
| 默认分支 | main |
| .gitignore | 已配置忽略 venv/、__pycache__/、.trae/、.vscode/ 等 |
| 数据库 | database/finderos.db 已包含在仓库中 |
| 文档 | docs/ 已包含在仓库中 |

---

*文档版本：v0.3 | 更新日期：2026-07-15*
