# Riya Dev
# 3/2/2021

# Crosswrd Puzzle Rules
#     Crosswords are symmetric with respect to their center (Rotation by 180 degrees produces the same blocked positions)
#     Every open square appears in both a horizontal and vertical word
#     Every word is at least 3 characters
#     No word in the crossword may happen twice.
#     The open squares are connected.

# Sample Input: file.py heightxwidth dict.txt #ofBlocks HVposxHposWord VVposxHposWord
'''
4x4 2 scrabble.txt v0x0yes
4x4 0 scrabble.txt V0x0come v0x1here h0x2ERS
'''

import sys; args = sys.argv[1:]
import re, random # os
# print(args)

# constants
blockchar = '#' # blocked square (black square)
openchar = '-' # open square (not decided yet)
protectedchar = '~' # reserved for word characters
counter = 0
# retest = [r"^\d+x\d+$", r"^\d+$", r"^\w+\.txt$", r"^v\d+x\d+\w+$", r"^h\d+x\d+\w+$"] # dimensions, num blocks, file, vertical, horizontal
# retest = [r"^\d+x\d+$", r"^\d+$", r"^\w+\.txt$", r"^v\d+x\d+\w+|v\d+x\d+(\w*#*)*$", r"^h\d+x\d+\w+|h\d+x\d+(\w*#*)*$"]
retest = [r"^\d+x\d+$", r"^\d+$", r"^\w+\.txt$", r"^v\d+x\d+.*$", r"^h\d+x\d+.*$"]

# variables
board = []
height = 0
width = 0
block_count = 0
file_name = 0

# methods
#def initialize(board):
#   height = int(args[0][0])
#   width = int(args[0][2])
#   # for x in range(height*width):
#   # board += "-"
#   row = []

#   for h in range(height):
#      for w in range(width):
#         row.append("-")
#      board.append(row)
#      row = []
#   print(board)

def display(board):
   for r in board:
      for c in r:
         print(c, end = " ")
      print()
        
   #for h in range(height):
   #   print()
   #   for w in range(width):
   #      print(board[h][w])

def makeboard(board):
   for arg in args:
      #if os.path.isfile(arg):
      #   return True
         
      for k, r in enumerate(retest):
         match = re.search(r, arg, re.I)
         if k == 0 and match != None: # dimensions
            height, width = arg.split('x') # set global value
            height = int(height)
            width = int(width)
            
            row = []
            for h in range(height):
               for w in range(width):
                  row.append("-")
               board.append(row)
               row = []
                     
         elif k == 1 and match != None: # number of blocks
            block_count = arg
            block_count = int(block_count)

            if block_count == height * width:
               for h in range(height):
                  for w in range(width):
                     board[h][w] = blockchar
            
         elif k == 2 and match != None: # word list file
            file_name = arg
            
         elif k == 3 and match != None: # vertical
            arg = arg[1:]
            row, p2 = arg.split('x')
            # print("vertical", p2, re.findall(r"^(\d+)(.*)$", p2))
            res = re.findall(r"^(\d+)(.*)$", p2)[0] #re.findall(r"^(\d+)(\w+?)$", p2)[0]
            col, word = res
            row = int(row)
            col = int(col)
            length = len(word)
            
            charnum = 0
            for r in range(row, row + length):
               board[r][col] = word[charnum].upper()
               charnum += 1
            
         elif k == 4 and match != None: # horizontal
            arg = arg[1:]
            row, p2 = arg.split('x')
            # print("horizontal", re.findall(r"^(\d+)(.*)$", p2))
            res = re.findall(r"^(\d+)(.*)$", p2)[0] # res = re.findall(r"^(\d+)(\w+?)$", p2)[0]     |     re.findall(r"^(\d+)(\w*#*)$", p2)[0]
            col, word = res
            
            row = int(row)
            col = int(col)
            length = len(word)
            
            charnum = 0
            for c in range(col, col + length):
               board[row][c] = word[charnum].upper()
               charnum += 1
      
      #xw = blockchar*(width+3)
      #xw +=(blockchar*2).join([xword[p:p+width] for p in range(0,len(xword),width)])
      #xw += blockchar*(width+3)

def cleanprotected():
   return

def addblockedsquare():
   return
   
def area_fill(board, sp, dirs = [-1, width, 1, -1*width]):
   if sp < 0 or sp >= len(board):
      return board
   if board[sp] in {openchar, protectedchar}:
      board = board[0:sp] + '?' + board[sp+1:]
      for d in dirs:
         if d == -1 and sp % width == 0:
            continue #left edge
         if d == 1 and sp+1 % width == 0:
            continue #right edge
         board = area_fill(board, sp+d, dirs)
   return board

def main():
   # initialize(board)
   makeboard(board)
   display(board)
   # print(height, width)
   
main()

# Test Cases

# test 1: 5x5 16 dct20k.txt
   
# test 2: 6x6 0 dct20k.txt V0x0Carmel V0x5Signal
    
# test 3: 9x9 12 dct20k.txt V0x1Nsw
    
# test 4: 15x15 39 dct20k.txt H0x0Mute V0x0mule V10x13Verse H7x5# V3x4# H6x7# V11x3#
    
# test 5: 10x12 32 dct20k.txt V6x0# V9x3# H3x8# V0x6Continuity
    
# test 6: 9x9 14 dct20k.txt V0x4con V6x4ate
    
# test 7: 13x13 32 dct20k.txt H1x4#Toe# H9x2# V3x6# H10x0Scintillating V0x5stirrup H4x2##Ordained V0x1Rudy V0x12Upc V5x0pew    
    
# test 8: 13x13 32 dct20k.txt V2x4# V1x9# V3x2# h8x2#moo# v5x5#two# h6x4#ten# v3x7#own# h4x6#orb# H12x4Omar
    
# test 9: 13x13 25 dct20k.txt H6x4no#on v5x5rot v0x0instep h0x4trip H0x9Calf V0x12foot
    
# test 10: 9x24 36 dct20k.txt h4x9n# h3x6s# h2x6# v2x0pan V5x1#b V8x20p
    
# test 11: 14x14 108 dct20k.txt V3x2 h2x3 h4x4 h7x4 h9x5 h8x4