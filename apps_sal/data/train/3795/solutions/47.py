import unittest


def combat(health, damage):
    if health <= damage:
        return 0
    return health - damage


class TestCombat(unittest.TestCase):
    def test_should_return_0_when_given_damage_is_greater_than_health(self):
        self.assertEqual(combat(health=20, damage=30), 0)

    def test_combat_with_given_health_is_greater_than_damage(self):
        self.assertEqual(combat(health=100, damage=5), 95)
