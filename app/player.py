class Player:

    _unique_id: str = None
    _name: str = None

    @property
    def uid(self) -> str:
        if not self._unique_id:
            raise NotImplementedError('Error: No Unique ID provided.')
        return self._unique_id

    @property
    def name(self) -> str:
        if not self._name:
            raise NotImplementedError('Error: No Name provided.')
        return self._name

    def __init__(self, unique_id: str, name: str) -> None:
        self._unique_id = unique_id
        self._name = name

    def __str__(self) -> str:
        return f'Player:\n\tUID: {self.uid}\n\tName: {self.name}'
