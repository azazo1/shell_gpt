from pathlib import Path
from typing import Dict, List, Optional

from ..config import cfg
from ..role import SystemRole
from .handler import Handler

CHAT_CACHE_LENGTH = int(cfg.get("CHAT_CACHE_LENGTH"))
CHAT_CACHE_PATH = Path(cfg.get("CHAT_CACHE_PATH"))


class DefaultHandler(Handler):
    def __init__(self, role: SystemRole, markdown: bool) -> None:
        super().__init__(role, markdown)
        self.role = role

    def make_messages(
        self, prompt: str, history: Optional[List[Dict[str, str]]]=None
    ) -> List[Dict[str, str]]:
        messages = [
            {
                "role": "system",
                "content": self.role.role.format(text_lang=cfg.get("TEXT_LANG")),
            },
        ]
        if history:
            messages.extend(history)
        messages.append({"role": "user", "content": prompt})
        return messages
