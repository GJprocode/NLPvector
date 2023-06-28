import spacy
import numpy as py

nlp = spacy.load("en")

#Creating an empty dictionary
d = {}

#Reading file
myfile = open("movies.txt").read()
myfile = myfile.split('\n')
myfile.pop()
#Saving contents of file in a dictionary
for i in myfile:
  d[i.split(":")[0]] = i.split(":")[1]



l1 = []
for i in d.values():
  sentence_to_compare = '''Will he save their world or destroy it? 
  When the Hulk becomes too dangerous for the Earth, the 
  Illuminati trick Hulk into a shuttle and launch him into space 
  to a planet where the Hulk can live in peace. Unfortunately, 
  Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator'''

  model_sentences = nlp(sentence_to_compare)



#Comparing each movie description with the given dexcription to find the closest simillarity
similarity = nlp(i).similarity(model_sentences)
print(i + "-" + str(similarity))
l1.append(similarity)

movie_title = []
for i in d.keys():
  movie_title.append(i)
#Printing the movie title
print(movie_title[l1.index(max(l1))])
