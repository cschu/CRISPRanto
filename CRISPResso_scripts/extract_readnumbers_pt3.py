#!/usr/bin/env python
# coding=utf-8
import sys
import re
import os

# print('\t'.join(('sample', 'reads_with_ins', 'reads_with_del', 'reads_with_sub', 'reads_total')))

with open(sys.argv[1]) as _in:
    # oleg/CRISPResso_on_1_part2_rep1_AGGCAGAACTCTCTAT_L001_R1_1_part2_rep1_AGGCAGAACTCTCTAT_L001_R2/Quantification_of_editing_frequency.txt
    # oleg/CRISPResso_on_32_and_31_part3_rep1_GTAGAGGACTCTCTAT_L001_R1_32_and_31_part3_rep1_GTAGAGGACTCTCTAT_L001_R2/
    sample = '_'.join(sys.argv[1].split('/')[1].split('_')[2:7])
    next(_in)
    next(_in)
    _ins, _del, _sub = (item for item in next(_in).replace('(', '').split(' ') if item.isdigit())
    next(_in)
    next(_in)
    next(_in)
    total = next(_in).split(':')[1].split(' ')[0]
    print('\t'.join((sample, _ins, _del, _sub, total)))


"""
Quantification of editing frequency:
	- Unmodified:6838 reads
	- NHEJ:60 reads (22 reads with insertions, 10 reads with deletions, 28 reads with substitutions)
	- HDR:0 reads (0 reads with insertions, 0 reads with deletions, 0 reads with substitutions)
	- Mixed HDR-NHEJ:0 reads (0 reads with insertions, 0 reads with deletions, 0 reads with substitutions)

Total Aligned:6898 reads 
"""
