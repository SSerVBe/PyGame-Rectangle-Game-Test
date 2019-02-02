import pygame

import main

szWidth = 1120
szHeight = 630

print(":::::  LOG  :::::")

print("Start initializing...")
run = main.main(szWidth, szHeight)
print("End initializing")

print("Starting game")
run.runGame()