# Name: Brieanna Benson
# Evergreen Login: benbri03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys
import math

###########################################################################
### Functions
###

# compares two strings and returns a 1 if they match
def dna_compare(x, y):
    if x == y:
        return 1
    else:
        return 0


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
sum_total = 0

# Number of A, T, C, and G seen.
c_count = 0
g_count = 0
a_count = 0
t_count = 0

# calculated results
atgc_ratio = 0
gc_class = 'none'

# for each base pair in the string,
for bp in seq:
    
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # compare each string to see if it matches any of the four characters
    c_count += dna_compare(bp, 'C')
    g_count += dna_compare(bp, 'G')
    a_count += dna_compare(bp, 'A')
    t_count += dna_compare(bp, 'T')

# sums up all the four types
sum_total = a_count + t_count + g_count + c_count

# create content ratios for each pair of DNA types
gc_content = float(g_count + c_count) / sum_total
at_content = float(a_count + t_count) / sum_total

# calculate the ratio of AT to GC
atgc_ratio = at_content / gc_content

# compares the ratio to numbers and defines its gc class
if atgc_ratio < 1:
    gc_class = 'High GC Content'
elif atgc_ratio >= 1 and atgc_ratio < 2:
    gc_class = 'Moderate GC Content'
else:
    gc_class = 'Low GC Content'

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G-count:', g_count
print 'C-count:', c_count
print 'A-count:', a_count
print 'T-count:', t_count
print 'Sum count:', sum_total
print 'Total count:', total_count
print 'Seq length:', total_count
print 'AT/GC Ratio:', atgc_ratio
print 'GC Classification:', gc_class