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
        self.font = pygame.font.SysFont("nanum", 32, 1, 0)
        self.change_speed_x = random.randint(-2, 2)
        if self.change_speed_x == 0:
            self.change_speed_x = 2
        self.change_speed_y = random.randint(-2, 2)
        if self.change_speed_y == 0:
            self.change_speed_x = 2


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
                self.blocki.rect.x = random.randrange(self.szWidth - 100)
                self.blocki.rect.y = random.randrange(self.szHeight - 50)
                self.block_group_list[h].add(self.blocki)
                self.all_sprites_list.add(self.blocki)
        self.player = self.bc.Block(self.WHITE, 20, 15)
        self.all_sprites_list.add(self.player)
        self.red_score = 50
        self.blue_score = 50

        self.movex = 0

        self.carry_block_list = []
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
                    self.carry_block_list = self.blocks_hit_list

                if event.type == pygame.MOUSEBUTTONUP:
                    self.carry_block_list = []
                mouse_pressed = pygame.mouse.get_pressed()

            #Source
            self.gamepad.fill(self.BLACK)
            self.rand = random.randint(0, 24)
            for blocks in self.blue_block_list:
                blocks.rect.x += self.change_speed_x
                blocks.rect.y += self.change_speed_y
                if blocks.rect.x > self.szWidth - 20 or blocks.rect.x < 0:
                    self.change_speed_x = self.change_speed_x * -1
                if blocks.rect.y > self.szHeight - 15 or blocks.rect.y < 0:
                    self.change_speed_y = self.change_speed_y * -1
            for blocks in self.red_block_list:
                blocks.rect.x += self.movex
                if blocks.rect.x  < 0:
                    blocks.rect.x = 0
                if blocks.rect.x >= self.szWidth - 10:
                    blocks.rect.x = self.szWidth - 10
            self.pos = pygame.mouse.get_pos()
            self.diff_x = self.player.rect.x - self.pos[0]
            self.diff_y = self.player.rect.y - self.pos[1]
            self.blocks_hit_list = pygame.sprite.spritecollide(self.player, self.all_sprites_list, False)
            for carryingBlock in self.carry_block_list:
                carryingBlock.rect.x -= self.diff_x
                carryingBlock.rect.y -= self.diff_y
            self.player.rect.x = self.pos[0]
            self.player.rect.y = self.pos[1]
            self.text = self.font.render("x::"+str(self.pos[0])+"\ty::"+str(self.pos[1])+"\nplayer::("+str(self.player.rect.x)+","+str(self.player.rect.y)+")", 1, self.WHITE)
            self.text2 = self.font.render("x_distance::"+str(self.diff_x)+"\ty_distance::"+str(self.diff_y), 1, self.WHITE)
            self.text3 = self.font.render("Red Left::"+str(len(self.red_block_list))+" \t Blue Left::"+str(len(self.blue_block_list)), 1, self.WHITE)
            self.gamepad.blit(self.text, (0, 0))
            self.gamepad.blit(self.text2, (0, 16))
            self.gamepad.blit(self.text3, (0, 32))
            red_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.red_block_list, False)
            blue_blocks_hit_list = pygame.sprite.spritecollide(self.player, self.blue_block_list, False)
            self.all_sprites_list.draw(self.gamepad)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit() #end