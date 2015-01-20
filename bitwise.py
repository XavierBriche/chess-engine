#!/usr/bin/env python
# Filename: bitwise.py
# -*- coding: utf-8 -*-

import constants as const

class Bitwise(object):
    def __init__(self, bitboard):
        self._bb = bitboard
    def rev(self):
        self._rev = ((self._bb & 0x5555555555555555) << 1) |\
                            ((self._bb & 0xAAAAAAAAAAAAAAAA) >> 1)
        self._rev = ((self._rev & 0x3333333333333333) << 2) |\
                            ((self._rev & 0xCCCCCCCCCCCCCCCC) >> 2)
        self._rev = ((self._rev & 0x0F0F0F0F0F0F0F0F) << 4) |\
                            ((self._rev & 0xF0F0F0F0F0F0F0F0) >> 4)
        self._rev = ((self._rev & 0x00FF00FF00FF00FF) << 8) |\
                            ((self._rev & 0xFF00FF00FF00FF00) >> 8)
        self._rev = ((self._rev & 0x0000FFFF0000FFFF) << 16) |\
                            ((self._rev & 0xFFFF0000FFFF0000) >> 16)
        self._rev = ((self._rev & 0x00000000FFFFFFFF) << 32) |\
                            ((self._rev & 0xFFFFFFFF00000000) >> 32)
        return self._rev

    def cw90(self):
        self._rot_cw90 = 0
        for bit_ind in range(0, 64):
           self._rot_cw90 += bool(self._bb & 1 << bit_ind)*\
                                         (2**(const.ro90_squares[bit_ind]))
        return self._rot_cw90

    def acw90(self):
        self._rot_acw90 = 0
        for bit_ind in range(0, 64):
           self._rot_acw90 += bool(self._bb & 1 << bit_ind)*\
                                            (2**(const.squares_ro90[bit_ind]))
        return self._rot_acw90

    def acw45(self):
        self._rot_acw45 = 0
        for bit_ind in range(0, 64):
           self._rot_acw45 += bool(self._bb & 1 << bit_ind)*\
                                            (2**(const.squares_ro45[bit_ind]))
        return self._rot_acw45

    def cw135(self):
        self._rot_acw135 = 0
        for bit_ind in range(0, 64):
           self._rot_acw135 += bool(self._bb & 1 << bit_ind)*\
                                            (2**(const.squares_ro135[bit_ind]))
        return self._rot_acw135


    def cw45(self):
        self._rot_cw45 = 0
        for bit_ind in range(0, 64):
           self._rot_cw45 += bool(self._bb & 1 << bit_ind)*\
                                            (2**(const.ro45_squares[bit_ind]))
        return self._rot_cw45

    def acw135(self):
        self._rot_cw135 = 0
        for bit_ind in range(0, 64):
           self._rot_cw135 += bool(self._bb & 1 << bit_ind)*\
                                            (2**(const.ro135_squares[bit_ind]))
        return self._rot_cw135

    def rank(self):
        return const.bits_ranks[self.bit_index(self._bb)]

    def files(self, bb):
        return const.bits_files[self.bit_index(self._bb)]

    def bit_index(self):
        return int(log(self._bb)/log(2))

    def bit_to_int(self, array):
        num = 0
        for a in array:
            num +=2**a
        return num
