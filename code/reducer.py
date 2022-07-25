#
# Reducer for Word Count application
# @date 07/06/22
#

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=line.lower()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
      count = int(count)
    except ValueError:
      continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print ('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    print( '%s\t%s' % (current_word, current_count))



