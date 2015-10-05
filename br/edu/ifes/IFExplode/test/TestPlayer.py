__author__ = 'Matheus'


import unittest
from br.edu.ifes.IFExplode.cdp.Player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    #Testa se o objeto player tem imagem
    def testPlayerHasImage(self):
        assert self.player.image != None, "Player image is None"

    #Testa se player tem rect
    def testPlayerHasRectangle(self):
        assert self.player.rect != None, "Player rectangle is None"

    def testPlayerPositioning(self):
        self.player.set_position(20,20)
        assert self.player.rect.x == 20 & self.player.rect.y ==20



if __name__=="main":
    unittest.main()