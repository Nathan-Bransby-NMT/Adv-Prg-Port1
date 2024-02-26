import unittest
from app import PlayerList, PlayerNode, Player


class PlayerListUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player_list = PlayerList()
        self.test_uid: str = "P1"
        self.test_player_name: str = "Player1"
        self.test_player = Player(self.test_uid, self.test_player_name)

    def test_player_prepending_into_empty_list(self):
        """Tests player insertion into the head of an empty PlayerList"""
        self.player_list.prepend(self.test_player)  # Insert a player into the list
        self.assertIsNotNone(self.player_list.head, "No value assigned to the head after insertion.")
        self.assertIsNotNone(self.player_list.tail, "No value assigned to the tail after insertion to an empty list.")

    def test_player_prepending_into_populated_list(self):
        """Tests player insertion into the head of an already populated PlayerList"""
        player2 = Player(self.test_uid, self.test_player_name)  # Test player 2.
        player1 = self.test_player  # Test player 1.
        self.player_list.prepend(player1)  # Insert player 1
        current_head = self.player_list.head  # The value of the head before 2nd insertion.
        self.player_list.prepend(player2)  # insert player 2
        self.assertNotEqual(current_head, self.player_list.head, "The head value has not been updated after insertion.")
        self.assertEqual(self.player_list.head.next, current_head,
                         "The head node does not point to the next node after insertion.")


if __name__ == '__main__':
    unittest.main()
