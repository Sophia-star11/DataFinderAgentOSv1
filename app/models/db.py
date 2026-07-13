import os
import sqlite3

def project_root():
    # 当前项目的 ../DataFinderAgentOS/
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

DB_PATH = os.path.join(project_root(), "database", "finderos.db")

def get_connection():
    # 获得一个数据库的连接，用于操作数据库完成事务和数据操作
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            )
            """
        )