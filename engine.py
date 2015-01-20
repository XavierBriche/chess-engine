#!/usr/bin/env python
# Filename: engine.py
# -*- coding: utf-8 -*-

import sys
import chessboard as cb
import notation as nt
import attacks as attk

if sys.version > '3':
    unicode = str

class ChessEngine(object):
        global slider
        global board

class Initialise(ChessEngine):
    """Set rank and file masks, bitboard rotators
        bitboard =  64 bits (squares)
    """
    def __init__(self):
        # pieces starting positions
        self._wp_init = 0x000000000000ff00
        self._wn_init = 0x0000000000000042
        self._wb_init = 0x0000000000000024
        self._wr_init = 0x0000000000000081
        self._wq_init = 0x0000000000000010
        self._wk_init = 0x0000000000000008
        self._bp_init = 0xff000000000000
        self._bn_init =   0x4200000000000000
        self._bb_init = 0x2400000000000000
        self._br_init = 0x8100000000000000
        self._bq_init  = 0x1000000000000000
        self._bk_init   = 0x800000000000000
        self._board ={0 : self._bp_init,
                                  1: self._wp_init,
                                  2 : self._bn_init,
                                  3 : self._wn_init,
                                  4: self._bb_init,
                                  5 : self._wb_init,
                                  6 : self._br_init,
                                  7 : self._wr_init,
                                  8 : self._bq_init,
                                  9 : self._wq_init, 
                                  10 : self._bk_init,
                                  11 : self._wk_init,
                                  12 : 0,
                                  13 : 0}

class Display(ChessEngine):
    
    def __init__(self, board):
        self._board = nt.Bitboard().to_fen(board)
        
    def chessboard(self):
            self._chessboard = cb.ChessBoard(self._board)
            self._chessboard.create_chessboard()
            self._chessboard.root.title("Chessboard")
            self._chessboard.root.mainloop()
            
initialised = Initialise()
board = initialised._board
board = { 0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 2**8+2**11, 
          5 : 0, 6 : 0, 7 : 0, 8: 0, 9 : 0, 10 : 0, 
          11 : 0, 12 : 0, 13: 0}
ply =1
white_occupancy = 0
black_occupancy = 0
if ply & 1:
    for piece in board:
        if piece & 1:
            white_occupancy = board[piece] | white_occupancy
        else:
            black_occupancy = board[piece] | black_occupancy
board = { 0 : 0,
                  1 : 2**54+2**53+2**52+2**51+2**50+2**49,
                    2 : 0, 3 : 0, 4 : 2**8+2**11, 5 : 0, 6 : 0, 7 : 0, 8: 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13: 0}
board[13] = 0
board[12] = black_occupancy | white_occupancy
Display(board).chessboard()

    
