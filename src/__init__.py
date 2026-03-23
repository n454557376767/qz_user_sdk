# src/__init__.py
from .core import post

class QzClient:
    def __init__(self, token = None):
        self.token = token
    @property
    def post(self):
        from .core.post import Post  # 延迟加载
        return Post(self.token)        