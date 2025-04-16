import pygame
from pygame.locals import *
import pygame.gfxdraw
import time
from math import inf
import pygame, sys
from mancala.board import Board, Game
from mancala.play import Play

import math
pygame.init()

screen_width = 1000
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

def get_fosse_from_mouse(pos,game, joueur):
    list = game.state.possibleMoves(joueur)
    for cle in list:
        Axis = game.state.boardAxis[cle]
        distance = math.sqrt((pos[0]-Axis[0])**2 + (pos[1]-Axis[1])**2)
        if distance <= 60 :
            return cle

bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (50,205,50)
gris = (200,200,200)
backcolour = pygame.color.Color(100,0,0)
x = 1000/8
y = 80
board = Board()
game = Game(board)
play = Play()
player = 1

#define global variable
clicked = False

class button():
		
	#colours for button and text
	button_col = (255, 0, 0)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = black
	width = 230
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

play_again = button(385, 400, 'Play again')



def execute():
    global player
    global board
    global game
    while True:
        # lose.pause()
        pygame.mixer.stop()
        # board.drawTurn(player, screen)
        screen.fill(backcolour)
        board.drawBoard(screen)
        if player == 1:
            board.colorPossibleMoves(screen,player)
        board.drawTurn(player, screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
                pos = pygame.mouse.get_pos()
                # if pos is not None :
                fosse = get_fosse_from_mouse(pos,game, player)
                # print(fosse)
                if fosse != None : 
                    # board.drawTurn(player, screen)
                    if game.gameOver() == False :
                        player = game.state.doMove(player, fosse)
                        board.drawBoard(screen)
                        pygame.display.update()
                        time.sleep(1)
                    else:
                        print('game Over')
        
            
        if player == -1 :
            board.drawTurn(player, screen)
            bestValue, bestPit =play.MiniMaxAlphaBetaPruning(game, player, 5, -inf, inf)
            if bestPit != None :
                player =  game.state.doMove(player, bestPit)
                # print(player)
                # print(game.state.board['2'])
                board.drawBoard(screen)
                pygame.display.update()
                time.sleep(1)

        if game.gameOver():
            board.drawBoard(screen)
            pygame.display.update()
            time.sleep(2)
            while True :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                winer, score = game.findWinner()
                screen.fill(backcolour)
                pygame.draw.rect(screen, gris, (150 , 30, 680, 500),  0,20)
                # kk++++++++++++==
                # lose.play()
                # pygame.mixer.music.play(-1)
                # jj//////////////////////////////////////////
                if play_again.draw_button():
                    print('dkhol')
                    board = Board()
                    game = Game(board)
                    player = 1
                    execute()
                # jj/////////////////////////////////////////
                font = pygame.font.Font('freesansbold.ttf', 48)
                if winer == -1:
                    # pygame.mixer.music.play()
                    text = font.render('You are lose, your Score: '+str(game.state.board['1']), True, red )
                    text4 = font.render('Computer score: '+str(score), True, black)
                    textRect4 = text4.get_rect()
                    textRect4.center = (475,150)
                    screen.blit(text4, textRect4)
                elif winer == 1:
                    text = font.render('You are win, your Score: '+str(score), True, green )
                    text2 = font.render('Congratulation .. !', True, black )
                    text3 = font.render('Computer Score: '+str(game.state.board['2']), True, red)
                    textRect3 = text3.get_rect()
                    textRect3.center = (460,300)
                    textRect2 = text2.get_rect()
                    textRect2.center = (475,150)
                    screen.blit(text2, textRect2)
                    screen.blit(text3, textRect3)
                else:
                    text = font.render('No one win, your score: '+str(score), True, green )
                textRect = text.get_rect()
                textRect.center = (480,250)
                screen.blit(text, textRect)
                # pygame.mixer.music.fadeout(3000)
                # pygame.mixer.Sound.stop()
                pygame.display.update()

def execute2():
    global player
    global board
    global game
    while True:
        # lose.pause()
        pygame.mixer.stop()
        # board.drawTurn(player, screen)
        screen.fill(backcolour)
        board.drawBoard(screen)
        # if player == 1:
        # board.colorPossibleMoves(screen,player)
        # board.drawTurnComputerVsComputer(player, screen)
        # time.sleep(1.5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # if event.type == pygame.MOUSEBUTTONDOWN and player == 1:
            #     pos = pygame.mouse.get_pos()
            #     # if pos is not None :
            #     fosse = get_fosse_from_mouse(pos,game, player)
            #     # print(fosse)
            #     if fosse != None : 
            #         # board.drawTurn(player, screen)
            #         if game.gameOver() == False :
            #             player = game.state.doMove(player, fosse)
            #             board.drawBoard(screen)
            #             pygame.display.update()
            #             time.sleep(1)
            #         else:
            #             print('game Over')
        
        if player == 1:
            board.drawTurnComputerVsComputer(player, screen)
            board.colorPossibleMoves(screen,player)
            pygame.display.update()
            time.sleep(1)
            # bestValue, bestPit =play.minimax(game, player, 2, -inf, inf)
            bestValue, bestPit =play.MiniMaxAlphaBetaPruning(game, player, 5, -inf, inf)
            if bestPit != None :
                player =  game.state.doMove(player, bestPit)
                # print(player)
                # print(game.state.board['2'])
                board.drawBoard(screen)
                pygame.display.update()
                time.sleep(1)
            
        if player == -1 :
            board.drawTurnComputerVsComputer(player, screen)
            board.colorPossibleMoves(screen,player)
            pygame.display.update()
            time.sleep(1)
            # bestValue, bestPit =play.minimax(game, player, 2, -inf, inf)
            bestValue, bestPit =play.MiniMaxAlphaBetaPruning2(game, player, 5, -inf, inf)
            if bestPit != None :
                player =  game.state.doMove(player, bestPit)
                # print(player)
                # print(game.state.board['2'])
                board.drawBoard(screen)
                pygame.display.update()
                time.sleep(1)

        if game.gameOver():
            board.drawBoard(screen)
            pygame.display.update()
            time.sleep(2)
            while True :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                winer, score = game.findWinner()
                screen.fill(backcolour)
                pygame.draw.rect(screen, gris, (80 , 30, 780, 500),  0,20)
                # kk++++++++++++==
                # lose.play()
                # pygame.mixer.music.play(-1)
                # jj//////////////////////////////////////////
                if play_again.draw_button():
                    print('dkhol')
                    board = Board()
                    game = Game(board)
                    player = 1
                    execute2()
                # jj/////////////////////////////////////////
                font = pygame.font.Font('freesansbold.ttf', 48)
                if winer == -1:
                    # pygame.mixer.music.play()
                    text = font.render('The winner: computer 2, score: '+str(score), True, green )
                    text4 = font.render('The loser: computer 1, score: '+str(game.state.board['1']), True, red)
                    textRect4 = text4.get_rect()
                    textRect4.center = (475,300)
                    screen.blit(text4, textRect4)
                elif winer == 1:
                    text = font.render('The winner: computer 1, score: '+str(score), True, green )
                    # text2 = font.render('Congratulation .. !', True, black )
                    text3 = font.render('The loser: computer 2, score: '+str(game.state.board['2']), True, red)
                    textRect3 = text3.get_rect()
                    textRect3.center = (460,300)
                    # textRect2 = text2.get_rect()
                    # textRect2.center = (475,150)
                    # screen.blit(text2, textRect2)
                    screen.blit(text3, textRect3)
                else:
                    text = font.render('No one win, score: '+str(score), True, green )
                textRect = text.get_rect()
                textRect.center = (480,250)
                screen.blit(text, textRect)
                # pygame.mixer.music.fadeout(3000)
                # pygame.mixer.Sound.stop()
                pygame.display.update()

player_computer = button(240, 300, 'You vs Computer')
computer_computer = button(500, 300, 'Computer vs Computer')

run = True
while run:
    screen.fill(gris)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Choice The mode of the match :", True, (0,0,0))
    textRect = text.get_rect()
    screen.blit(text,(330,200))

    if computer_computer.draw_button():
        execute2()

    if player_computer.draw_button():
        execute()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False	

    pygame.display.update()

pygame.quit()