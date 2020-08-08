numKeys = 88 # total number of keys on a piano
handSpan = 13 # hand can span this many piano keys
chordCount3 = 0 # number of possible 3-note chords
chordCount4 = 0 # number of possible 4-note chords
chordCount5 = 0 # number of possible 5-note chords

#create a file with a list of all the possible chords
file1 = open("chords.txt", "w")

# the first key can be anything on the piano keyboard
for firstKey in range(0, numKeys):
    # the second key must be higher than the 1st, and within a hand span of the 1st
    # but can't be higher than the highest key on the keyboard
    for secondKey in range(firstKey+1, min(firstKey+handSpan, numKeys)):
        # the third key must be higher than the 2nd, and within a hand span
        for thirdKey in range(secondKey+1, min(firstKey+handSpan, numKeys)):
            file1.write("{0} {1} {2}  \n".format(firstKey+1, secondKey+1, thirdKey+1))
            chordCount3 = chordCount3 + 1
            # the fourth key (if any) must be higher than the 3rd, and within a hand span
            for fourthKey in range(thirdKey+1, min(firstKey+handSpan, numKeys)):
                file1.write("{0} {1} {2} {3}  \n".format(firstKey+1, secondKey+1, thirdKey+1, fourthKey+1))
                chordCount4 = chordCount4 + 1
                # the fifth key (if any) must be higher than the 4th, and within a hand span
                for fifthKey in range(fourthKey+1, min(firstKey+handSpan, numKeys)):
                    file1.write("{0} {1} {2} {3} {4}  \n".format(firstKey+1, secondKey+1, thirdKey+1, fourthKey+1, fifthKey+1))
                    chordCount5 = chordCount5 + 1
                    #print("{0}, {1}, {2}".format(firstKey+1, secondKey+1, thirdKey+1))
file1.close()            
print("{0} total possible chords with one hand".format(chordCount3 + chordCount4 + chordCount5))
      