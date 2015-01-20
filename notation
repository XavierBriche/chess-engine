#!/usr/bin/python
# Filename: notation.py
# -*- coding: utf-8 -*-

class Bitboard(object):
    '''Translate position recorded in FICS notation into a dictionary of bitboards
        and vice versa.'''
    def __init__(self):
        self._bb_piece = 0
        self._pieces_bb={}
        self._fen = ''
        self._FICS = ['p', 'P', 'n', 'N', 'b', 'B', 'r',
                      'R', 'q', 'Q', 'k', 'K', 'x', 'X']
        
    def to_fen(self, allpieces_bbs):
        for bit_ind in range(0, 64):
            for piece in range(0, len(self._FICS)):
                if (allpieces_bbs[piece] & 1 << bit_ind):
                    self._fen += self._FICS[piece]
                    break
            else:
                self._fen += '-'
        print self._fen
        return self._fen
    
    def bitboards(self, fen, piece): #unmaintained
        for piece in self._FICS:
            self._bb_piece = 0
            for square in range(0, 64):
                if fen[square]==FICS[piece]:
                    self._bb_piece += 2**square
            self._pieces_bb[FICS[piece]]=self._bb_piece
        return self._pieces_bb
