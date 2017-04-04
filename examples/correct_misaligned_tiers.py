'''
Created on Apr 4, 2017

@author: Tim
'''
import os
from os.path import join

from praatio import praatio_scripts

path = join(".", "files")
outputPath = join(path, "aligned-tier_textgrids")

inputFN = join(path, "mary_misaligned.TextGrid")
outputFN = join(outputPath, "mary_aligned.TextGrid")
maxDifference = 0.01

if not os.path.exists(outputPath):
    os.mkdir(outputPath)

tg = praatio_scripts.alignBoundariesAcrossTiers(inputFN, maxDifference)
tg.save(outputFN)
