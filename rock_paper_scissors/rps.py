#!/usr/bin/python

import sys
import itertools

def rock_paper_scissors(n):
  # Your code here
  if n == 0:
    return [[]]

  plays = ['rock', 'paper', 'scissors']
  permutations = list(itertools.product(plays, repeat=n))
  return permutations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')