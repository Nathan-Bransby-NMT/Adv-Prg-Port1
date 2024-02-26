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
    def head(self, value: PlayerNode | None) -> None:
        if self._head is not None:
            value.next = self._head
            self._head.prev = value
        self._head = value

    @property
    def tail(self) -> PlayerNode | None:
        return self._tail

    @tail.setter
    def tail(self, value: PlayerNode | None) -> None:
        if self._tail is not None:
            value.prev = self._tail
            self._tail.next = value
        self._tail = value

    def __init__(self, player_data: list[Player] | None = None) -> None:
        self.prepend(player_data)

    def prepend(self, data: Player | list[Player]) -> None:
        """Inserts one or more players to the beginning of the list.

        Provides methodologies to add Players to the head of the list as apposed
        to appending the item at the tail of the list.

        Args:
            data (Player | list[Player]): The Player / Players to insert at the start of the list.

        """
        if isinstance(data, list):
            for player in data:
                self.prepend(player)
            return

        if self.tail is None:
            self.tail = data
        self.head = PlayerNode(data)

    def append(self, data: Player | list[Player]) -> None:
        """Inserts one or more Players to the end of the list.

        Provides methodologies to add Players to the tail of the list as apposed
        to prepending at the head of the list.

        Args:
            data (Player | list[Player]): The Player / Players to insert onto the end of the list.
        """
        if isinstance(data, list):
            for player in data:
                self.append(player)
            return

        if self.head is None:
            self.head = data
        self.tail = PlayerNode(data)

    def remove_from_head(self, count: int = None) -> None:
        """Delete one or more Players from the start of the list.

        Provides a method allowing you to remove a specified number of
        Players from the beginning of the list.

        Args:
            count (int): The number of players to remove from the beginning of the list.
                If no value is set, only the first element is removed. Defaults as None.

        Raises:
              IndexError: If the count is not None and less-than 0.
              ValueError: If the list doesn't contain any elements.
        """
        if self.head is None:
            raise ValueError("Error: Unable to remove from an empty list.")

        if count:
            if count < 0:
                raise IndexError("Error: The count must be a positive integer.")
            try:
                for i in range(count):
                    self.remove_from_head()
                return None
            except ValueError:
                return None

        self._head = self._head.next
        if self.head is not None:
            self._head.prev = None

    def remove_from_tail(self, count: int = None) -> None:
        """Delete one or more Players from the end of the list.

        Provides a method allowing you to remove a specified number of
        Players from the end of the list.

        Args:
            count (int): The number of players to remove from the end of the list.
            If no value is set, only the end element will be removed. Defaults as None.

        Raises:
            IndexError: If the value count is not None less-than 0.
            ValueError: If the list doesn't contain any elements.
        """
        if self.tail is None:
            raise ValueError("Error: Unable to remove from an empty list.")

        if count:
            if count < 0:
                raise IndexError("Error: The count must be a positive integer.")
            try:
                for i in range(count):
                    self.remove_from_head()
                return None
            except ValueError:
                return None

        self._tail = self._tail.prev
        if self.tail is not None:
            self._tail.next = None
