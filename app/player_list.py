from typing import Any
from player_node import PlayerNode, Player


class PlayerList:

    _head: PlayerNode = None

    @property
    def is_empty(self) -> bool:
        return self._head is None

    @property
    def head(self) -> PlayerNode | None:
        return self._head

    @head.setter
    def head(self, value: PlayerNode) -> None:
        if self._head is not None:
            value.next = self._head
            self._head.prev = value
        self._head = value

    def __init__(self, player_data: list[Player] | None = None) -> None:
        self.insert(player_data)

    def insert(self, data: Player | list[Player]) -> None:
        if isinstance(data, list):
            for player in data:
                self.insert(player)
            return
        self.head = PlayerNode(data)
