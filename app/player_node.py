from __future__ import annotations
from app.player import Player


class PlayerNode:

    _value: Player = None
    _next: PlayerNode = None
    _prev: PlayerNode = None

    @property
    def value(self) -> Player:
        return self._value

    @property
    def next(self) -> PlayerNode | None:
        return self._next

    @next.setter
    def next(self, value: PlayerNode) -> None:
        self._next = value

    @property
    def prev(self) -> PlayerNode | None:
        return self._prev

    @property
    def key(self) -> str:
        if not self.value:
            raise NotImplementedError("No player assigned to the node.")
        return self.value.uid

    @prev.setter
    def prev(self, value: PlayerNode) -> None:
        self._prev = value

    def __init__(self, player: Player) -> None:
        self._value = player

    def __str__(self) -> str:
        return f'Player Node containing {self.value}' \
            if self.value else "Empty Player Node"
