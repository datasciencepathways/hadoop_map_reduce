#
# Mapper for Word Count application
# @date 07/06/22
#

import sys
import io
import re
import nltk

nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords

# common words in English articles, common verbs etc. 
common_words = set(stopwords.words('english'))

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')


for line in input_stream:
  # remove begining and trailing whitespace 
  line = line.strip()

  line = re.sub(r'[^\w\s]', '',line)

  # convert everything to lower case 
  line = line.lower()

  # remove punctuations 
  for x in line:
    if x in punctuations:
      line=line.replace(x, " ") 

  # extract the words from the line     
  words=line.split()
  for word in words: 
    # skip common words
    if word not in common_words:
      print('%s\t%s' % (word, 1))
