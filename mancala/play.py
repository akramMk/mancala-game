import random
from math import inf
import time
import pygame
# from board import Game, Board
from copy import deepcopy

class Play:
    # def __init__(self, game):
    #     self.game = game

    #NegaMaxAlphaBetaPruning
    def NegaMaxAlphaBetaPruning (self, game, player, depth, alpha, beta):
        #game est une instance de la classe Game et player = COMPUTER ou HUMAN
        if game.gameOver() or depth == 1:
            bestValue = game.evaluate2(player)
            bestPit = None
            if player == 1:
                bestValue = - bestValue
            return bestValue, bestPit
        
        bestValue = -inf
        bestPit = None
        for pit in game.state.possibleMoves(player):
            
            child_game = deepcopy(game)
            player_turn =  child_game.state.doMove(player, pit)
            # print(game.state.board['A'])

            if player_turn == player:
                value, _ = self.NegaMaxAlphaBetaPruning (child_game, player, depth-1, -beta, -alpha) 
            else:
                value, _ = self.NegaMaxAlphaBetaPruning (child_game, -player, depth-1, -beta, -alpha) 
                
            value = - value
            if value > bestValue :
                bestValue = value
                bestPit =pit

            if bestValue > alpha :
                alpha = bestValue

            if beta <= alpha :
                break
        return bestValue, bestPit
    
    def MiniMaxAlphaBetaPruning(self,game, player, depth, alpha , beta ):
        if game.gameOver() or depth == 1:
            bestValue = game.evaluate2(player)
            bestPit = None
            # if player == 1:
            #     bestValue = - bestValue
            # print(str(bestPit)+ ',' +str(bestValue))
            return bestValue, bestPit

            
        if player == 1 :
                bestValue = -inf
                bestPit = None
                for pit in game.state.possibleMoves(player):
                    child_game = deepcopy(game)
                    player_turn =  child_game.state.doMove(player, pit)
                    if player_turn == player:
                        value, _ = self.MiniMaxAlphaBetaPruning(child_game, player, depth-1, alpha, beta) 
                    else:
                        value, _ = self.MiniMaxAlphaBetaPruning(child_game, -player, depth-1, alpha, beta) 
                    if value > bestValue :
                        bestValue = value
                        bestPit =pit
                    if value >= beta:
                        # return bestValue
                        break
                    if value > alpha:
                        alpha = value
                # print(str(bestPit)+ ',' +str(bestValue))
                # return bestValue, bestPit
            
        else:
                bestValue = inf
                bestPit = None
                for pit in game.state.possibleMoves(player):
                    child_game = deepcopy(game)
                    player_turn =  child_game.state.doMove(player, pit)
                    if player_turn == player:
                        value, test = self.MiniMaxAlphaBetaPruning(child_game, player, depth-1, alpha, beta) 
                    else:
                        value, test = self.MiniMaxAlphaBetaPruning(child_game, -player, depth-1, alpha, beta) 
                    if value < bestValue : 
                        bestValue = value
                        bestPit =pit
                    if value <= alpha:
                        # return bestValue
                        break
                    if value < beta:
                        beta = value
                # print(str(bestPit)+ ',' +str(bestValue))
                # return bestValue, bestPit
        return bestValue, bestPit

    def MiniMaxAlphaBetaPruning2(self,game, player, depth, alpha , beta ):
        if game.gameOver() or depth == 1:
            bestValue = game.evaluate3(player)
            bestPit = None
            # if player == 1:
            #     bestValue = - bestValue
            # print(str(bestPit)+ ',' +str(bestValue))
            return bestValue, bestPit

            
        if player == 1 :
                bestValue = -inf
                bestPit = None
                for pit in game.state.possibleMoves(player):
                    child_game = deepcopy(game)
                    player_turn =  child_game.state.doMove(player, pit)
                    if player_turn == player:
                        value, _ = self.MiniMaxAlphaBetaPruning2(child_game, player, depth-1, alpha, beta) 
                    else:
                        value, _ = self.MiniMaxAlphaBetaPruning2(child_game, -player, depth-1, alpha, beta) 
                    if value > bestValue :
                        bestValue = value
                        bestPit =pit
                    if value >= beta:
                        # return bestValue
                        break
                    if value > alpha:
                        alpha = value
                # print(str(bestPit)+ ',' +str(bestValue))
                # return bestValue, bestPit
            
        else:
                bestValue = inf
                bestPit = None
                for pit in game.state.possibleMoves(player):
                    child_game = deepcopy(game)
                    player_turn =  child_game.state.doMove(player, pit)
                    if player_turn == player:
                        value, test = self.MiniMaxAlphaBetaPruning2(child_game, player, depth-1, alpha, beta) 
                    else:
                        value, test = self.MiniMaxAlphaBetaPruning2(child_game, -player, depth-1, alpha, beta) 
                    if value < bestValue : 
                        bestValue = value
                        bestPit =pit
                    if value <= alpha:
                        # return bestValue
                        break
                    if value < beta:
                        beta = value
                # print(str(bestPit)+ ',' +str(bestValue))
                # return bestValue, bestPit
        return bestValue, bestPit
    
    def humanTurn(self,cle,game):
        list = game.state.possibleMoves(1)
        if cle in list :
            game.state.doMove(1,cle)


    def computerTrun(self, game):
        game.state.doMove(self.NegaMaxAlphaBetaPruning(self,"COMPUTER", 10, -inf, +inf),-1)
