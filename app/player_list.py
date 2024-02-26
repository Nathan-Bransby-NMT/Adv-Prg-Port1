from typing import Any
from app import PlayerNode, Player


class PlayerList:

    _head: PlayerNode | None = None
    _tail: PlayerNode | None = None

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

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail

    @tail.setter
    def tail(self, value: PlayerNode) -> None:
        if self._tail is not None:
            value.prev = self._tail
            self._tail.next = value
        self._tail = value

    def __init__(self, player_data: list[Player] | None = None) -> None:
        self.prepend(player_data)

    def prepend(self, data: Player | list[Player]) -> None:
        """Inserts one or more players to the head of the list.

        Provides methodologies to add players to the head of the list as apposed to appending at the tail.

        Args:
            data (Player | list[Player]):
                The Player / Players you want to insert at the head of the list.

        """
        if isinstance(data, list):
            for player in data:
                self.prepend(player)
            return
        if self.tail is None:
            self.tail = data
        self.head = PlayerNode(data)
