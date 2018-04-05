import unittest
from wardrobe import Wardrobe
from wardrobe import Material

class TestWardrobe(unittest.TestCase):
    def setUp(self):
        self.myWardrobe = Wardrobe("TestWardrobe", Material.CARBON_FIBRE)
        pass

    def test_opening(self):
        # test that you can't open if the wardrobe is broken
        self.myWardrobe._broken = True
        self.myWardrobe.open()
        self.assertEqual(self.myWardrobe._opened, False)

        # test that the wardrobe opens properly
        self.myWardrobe._broken = False
        self.myWardrobe.open()
        self.assertEqual(self.myWardrobe._opened, True)

    def test_closing(self):
        # test that you can't change the state if the wardrobe is broken
        self.myWardrobe._broken = False
        self.myWardrobe.open()
        self.myWardrobe._broken = True
        self.myWardrobe.close()
        self.assertEqual(self.myWardrobe._opened, True)

        # test that the wardrobe closes properly when it's not broken
        self.myWardrobe._broken = False
        self.myWardrobe.open()
        self.myWardrobe.close()
        self.assertEqual(self.myWardrobe._opened, False)

    def test_getting_in(self):
        # test that you can't get in if the wardrobe is broken
        self.myWardrobe._occupied = False
        self.myWardrobe.open()
        self.myWardrobe._broken = True
        self.myWardrobe.get_in()
        self.assertEqual(self.myWardrobe._occupied, False)

        # test that someone's in when you get in
        self.myWardrobe._occupied = False
        self.myWardrobe._broken = False
        self.myWardrobe.open()
        self.myWardrobe.get_in()
        self.assertEqual(self.myWardrobe._occupied, True)

    def test_getting_out(self):
        # test that you can't get out if the wardrobe is broken
        self.myWardrobe._occupied = True
        self.myWardrobe.open()
        self.myWardrobe._broken = True
        self.myWardrobe.get_out()
        self.assertEqual(self.myWardrobe._occupied, True)

        # test that no-one is in after you get out
        self.myWardrobe._occupied = True
        self.myWardrobe._broken = False
        self.myWardrobe.open()
        self.myWardrobe.get_out()
        self.assertEqual(self.myWardrobe._occupied, False)

    def test_kicking(self):
        # test that a wooden wardrobe breaks if you kick with force >3
        self.myWardrobe = Wardrobe("TestWardrobe", Material.WOOD)
        self.myWardrobe._broken = False
        self.myWardrobe.kick(4)
        self.assertEqual(self.myWardrobe._broken, True)

        # test that a wooden wardrobe does not break if you kick with force <= 3
        self.myWardrobe = Wardrobe("TestWardrobe", Material.WOOD)
        self.myWardrobe._broken = False
        self.myWardrobe.kick(3)
        self.assertEqual(self.myWardrobe._broken, False)

        # test that a glass wardrobe breaks if you kick with force >0
        self.myWardrobe = Wardrobe("TestWardrobe", Material.GLASS)
        self.myWardrobe._broken = False
        self.myWardrobe.kick(1)
        self.assertEqual(self.myWardrobe._broken, True)

        # test that a glass wardrobe does not break if you kick with force <1
        self.myWardrobe = Wardrobe("TestWardrobe", Material.GLASS)
        self.myWardrobe._broken = False
        self.myWardrobe.kick(0.5)
        self.assertEqual(self.myWardrobe._broken, False)

        # test that a carbon fibre wardrobe breaks if you kick with force >10
        self.myWardrobe = Wardrobe("TestWardrobe", Material.CARBON_FIBRE)
        self.myWardrobe._broken = False
        self.myWardrobe.kick(11)
        self.assertEqual(self.myWardrobe._broken, True)

        # test that a carbon fibre wardrobe does not break if you kick with force <= 10
        self.myWardrobe = Wardrobe("TestWardrobe", Material.CARBON_FIBRE)
        self.myWardrobe._broken = False
        self.myWardrobe.kick(10)
        self.assertEqual(self.myWardrobe._broken, False)

        #self.assertEqual(var,value)
        pass

if __name__ == "__main__":
    unittest.main()
