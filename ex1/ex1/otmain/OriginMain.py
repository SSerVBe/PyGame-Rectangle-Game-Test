import pygame
import random
import time

import block as bc

class main:
    def __init__(self, sizeW:int=1280, sizeH:int=720):
        self.bc = bc
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        print("Initializing...")
        pygame.init()
        print("Pygame module initialized")
        self.szWidth = sizeW
        self.szHeight = sizeH
        self.gamepad = pygame.display.set_mode((self.szWidth, self.szHeight))
        print("Created a window")
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("testLauncher by SSerVe")
        self.clock = pygame.time.Clock()


    def runGame(self):
        crashed = False
        ################
        self.red_block_list = pygame.sprite.Group()
        self.blue_block_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        self.color_list = [self.BLUE, self.RED]
        self.block_group_list = [self.blue_block_list, self.red_block_list]
        ################
        for h in range(2):
            for i in range(25):
                self.blocki = self.bc.Block(self.color_list[h], 20, 15)
                self.blocki.rect.x = random.randrange(self.szWidth)
                self.blocki.rect.y = random.randrange(self.szHeight)
                self.block_group_list[h].add(self.blocki)
                self.all_sprites_list.add(self.blocki)
        self.player = self.bc.Block(self.BLACK, 20, 15)
        self.all_sprites_list.add(self.player)
        self.red_score = 50
        self.blue_score = 50

        self.movex = 0

        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movex = -3
                    if event.key == pygame.K_RIGHT:
                        self.movex = 3
                if event.type == pygame.KEYUP:
                    self.movex = 0
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    blocks_hit_list = pygame.sprite.spritecollide(self.player, self.red_block_list, False)

            #Source
            self.gamepad.fill(self.WHITE)

            for blocks in self.red_block_list:
                blocks.rect.x += self.movex
                if blocks.rect.x  < 0:
                    blocks.rect.x = 0
                if blocks.rect.x >= self.szWidth - 10:
                    blocks.rect.x = self.szWidth - 10

            pos = pygame.mouse.get_pos()
            self.player.rect.x = pos[0]
            self.player.rect.y = pos[1]
            red_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.red_block_list, False)
            if red_blocks_hit_list:
                removeCnt = 0
                for removeSprite in self.red_block_list: 
                    if removeCnt % 2 == 0 and removeCnt > 0:
                        self.red_block_list.remove(removeSprite)
                        self.all_sprites_list.remove(removeSprite)
                    removeCnt += 1
            blue_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.blue_block_list, False)
            if red_blocks_hit_list:
                removeCnt = 0
                for removeSprite in self.red_block_list: 
                    if removeCnt % 2 == 0 and removeCnt > 0:
                        self.red_block_list.remove(removeSprite)
                        self.all_sprites_list.remove(removeSprite)
                    removeCnt += 1
            for block in red_blocks_hit_list:
                self.red_score = int(len(self.red_block_list))
                print("Red Blocks Left:" + str(len(self.red_block_list)))
            for block in blue_blocks_hit_list:
                self.blue_score = int(len(self.blue_block_list))
                print("Blue Blocks Left:" + str(len(self.blue_block_list)))
            if len(self.red_block_list) is 0 and len(self.blue_block_list) is 0:
                print("all blocks die")
                print("## Game Clear! ##")
                time.sleep(2)
                crashed = True
            self.all_sprites_list.draw(self.gamepad)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit() #end