#!/usr/bin/env python
# Filename: attacks.py
# -*- coding: utf-8 -*-

from math import log
import bitwise as btws
import constants as const


class Attacks(object):
#    global slider
    pass
    
class Attack(Attacks):
    ''' returns all the attacked squares for a piece on a square (slider)
        attack_bishop = PAttack(occupied squares).bishop_attack(slider).'''
    def __init__(self, slider):
        self._slider = slider
        self._r90_slider = btws.Bitwise(self._slider).cw90
        self._ar45_slider = btws.Bitwise(self._slider).acw45

    def bpawn_right(self):
        return self._slider >> 7 & const.notafile

    def bpawn_left(self):
            return self._slider >> 9 & const.nothfile
                     
    def wpawn_left(self):
            return self._slider << 7 & const.nothfile
        
    def wpawn_right(self):
                return self._slider << 9 & const.notafile
          
    def one_east(self):
        return self._slider << 1 & const.notafile

    def one_noea(self):
        return self._slider << 9 & const.notafile

    def one_north(self):
        return self._slider << 8

    def one_nowe(self):
        return self._slider << 7 & const.nothfile

    def one_west(self):
        return self._slider >> 1 & const.nothfile

    def one_sowe(self):
        return self._slider >> 9 & const.nothfile

    def one_south(self):
        return self._slider >> 8

    def one_soea(self):
        return self._slider >> 7 & const.notafile

    def el_noeaea(self):
        return self._slider<<10 & (const.notafile & const.notbfile)
      
    def el_nonoea(self):
         return self._slider<<17 & const.notafile

    def el_nonowe(self):
         return self._slider<<15 & const.nothfile

    def el_nowewe(self):
         return self._slider<<6 & (const.notgfile & const.nothfile)

    def el_sowewe(self):
         return self._slider>>10 & (const.notgfile & const.nothfile)

    def el_sosowe(self):
         return self._slider>>17 & const.nothfile

    def el_sosoea(self):
         return self._slider>>15 & const.notafile

    def el_soeaea(self):
         return self._slider>>6 & (const.notafile & const.notbfile)

#sliding pieces
    #bishop
    def mask_diag(self):
        for d in const.diag_masks:
            if btws.Bitwise(self._slider).bit_index() in d:
                break
        return btws.Bitwise(d).bit_to_int()

    def attack_adiag(self, occupied):
        self._r45_occupied = btws.Bitwise(occupied).acw45()
        self._r45_slid = btws.Bitwise(self._slider).acw45()
        self._ro_attack = self.attack_horizontal(self._r45_occupied,
                                                 self._r45_slid)
        return btws.Bitwise(self._ro_attack).cw45()

    def attack_diag(self, occupied):
        self._r135_occupied = btws.Bitwise(occupied).cw135()
        self._r135_slid = btws.Bitwise(self._slider).cw135()
        self._ro_attack = self.attack_horizontal(self._r135_occupied,
                                                 self._r135_slid)
        return btws.Bitwise(self._ro_attack).acw135()
    
    def mask_adiag(self):
        for d in const.adiag_masks:
            if btws.Bitwise(self._slider).bit_index() in d:
                break
        return btws.Bitwise(d).bit_to_int()
            
    def attack_horizontal(self, occupied, slid):
        self._rev_occupied= btws.Bitwise(occupied).rev()
        self._rev_slid = btws.Bitwise(slid).rev()
        attack = ((occupied - 2*slid)^\
                      (btws.Bitwise(self._rev_occupied - 2*self._rev_slid).rev())) &\
                      const.rank_masks[btws.Bitwise(slid).rank()]
        return attack
    
    def attack_vertical(self, occupied):
        self._r_occupied = btws.Bitwise(occupied).cw90()
        self._rev_r_occupied = btws.Bitwise(self._r_occupied).rev()
        self._r_slider = btws.Bitwise(self._slider).cw90()
        self._rev_r_slider = btws.Bitwise(self._r_slider).rev()
        attack = ((self._r_occupied - 2*self._r_slider)^ \
                       (btws.Bitwise(self._rev_r_occupied - 2*self._rev_r_slider).rev())) & \
                      const.rank_masks[btws.Bitwise(self._r_slider).rank()]                            
        return btws.Bitwise(attack).acw90()


class PAttack(Attacks):
    def __init__(self, occupied):
        self._occupied = occupied

    def bishop_attack(self, slider):
        bishop = Attack(slider)
        diag_mask = bishop.mask_diag()
        adiag_mask = bishop.mask_adiag()
        adiag_attack = bishop.attack_adiag(self._occupied)
        diag_attack = bishop.attack_diag(self._occupied)
        return (adiag_attack & adiag_mask) | (diag_attack & diag_mask)
    
    def rook_attack(self, slider):
        rook = Attack(slider)
        rank_attack = rook.attack_horizontal(self._occupied, slider)
        file_attack = rook.attack_vertical(self._occupied)
        return file_attack | rank_attack

    def queen_attack(self, slider):
        queen = Attack(slider)
        ranks_attack = queen.attack_horizontal(self._occupied, slider)
        files_attack = queen.attack_vertical(self._occupied)
        diag_mask = queen.mask_diag()
        adiag_mask = queen.mask_adiag()
        adiag_attack = queen.attack_adiag(self._occupied)
        diag_attack = queen.attack_diag(self._occupied)
        return files_attack | ranks_attack | \
                     (adiag_attack & adiag_mask) | (diag_attack & diag_mask)
    
    def knight_attack(self, slider):
        knight = Attack(slider)
        return knight.el_noeaea()|  knight.el_nonoea() | \
                    knight.el_nonowe() | knight.el_nowewe() | \
                    knight.el_sowewe() | knight.el_sosowe() | \
                    knight.el_sosoea() | knight.el_soeaea()

    def king_attack(self, slider):
        king = Attack(slider)
        return king.one_east() | king.one_noea() | king.one_soea() | \
                    king.one_north() | king.one_nowe() | king.one_west() | \
                    king.one_sowe() | king.one_west() | king.one_sowe() | \
                    king.one_south()

    def wpawn_attack(self, slider):
        white_pawn = Attack (slider)
        return (white_pawn.wpawn_left() | white_pawn.wpawn_right())

    def bpawn_attack(self, slider):
        black_pawn = Attack (slider)
        return (black_pawn.bpawn_left() | black_pawn.bpawn_right())                  

