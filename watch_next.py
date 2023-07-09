''' If spacy below is installed in your virtual environment with all modules
and still give the error import "spacy" could not be resolved,
just press Ctrl + Shift + P (win)/ cmd + Shift + P(macOS)
to open command pellet.
type "Python: Select Interpreter" and select this option when it appears. 
It will open a list of available Python interpreters.
Look for your virtual environment in the list and select it. 
It will typically be located in the .venv folder within your project directory
This will solve your issue, just work on the python interpreter with the
virtual environment with all modules installed'''


# imports the spacy library, a Natural language processing python library
import spacy

'''Code below loads the English language model (en_core_web_md) provided by spaCy. 
The model is responsible for processing text and generating word 
vectors that represent the meaning of words and sentences'''

nlp = spacy.load('en_core_web_md')

'''This line defines a function called find_similar_movie 
that takes a description parameter. 
this function will find the most similar movie based 
on the provided description'''

def find_similar_movie(description):
# Code below opens the movies.txt file in read mode and 
# reads its contents. It stores the content in the movie_data variable,
# which will be a list of strings where each string represents
# a line in the file.
    with open("movies.txt", "r") as file:
        movie_data = file.readlines()

# Code below iterates over each line in movie_data. 
# For each line, it splits the line into the movie title and description
#  based on the colon (:) separator. 
# The title is stored as the key in the 
# movies dictionary, and the description is stored as the 
# corresponding value. The strip() method is used to remove any leading 
# or trailing whitespace from the title and description strings.
    movies = {}
    for line in movie_data:
        title, desc = line.strip().split(":", 1)
        movies[title.strip()] = desc.strip()

# Below code calculate the similarity between the provided description 
# and each movie description in the movies dictionary.
#  It initializes an empty dictionary similarity_scores to store the 
# similarity scores. The nlp object is used to process the text and 
# generate word vectors for both the query description 
# and each movie description. The similarity() method is then 
# called on the query_vector and movie_vector to calculate the 
# similarity score, which is stored in the similarity_scores 
# dictionary with the movie title as the key.
    similarity_scores = {}
    query_vector = nlp(description)
    for title, desc in movies.items():
        movie_vector = nlp(desc)
        similarity_scores[title] = query_vector.similarity(movie_vector)

    # Find the movie with the highest similarity score
    most_similar_movie = max(similarity_scores, key=similarity_scores.get)
    return most_similar_movie

# Given Example Movie description to compare to other movies descriptions and calculate
# a recommended movie based on similarity 
description = '''Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the
Illuminati trick Hulk into a shuttle and launch him into 
space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold
into slavery and trained as a gladiator.'''

'''Below code finds the movie with the highest similarity score by using the max()
function on the similarity_scores dictionary. 
The key argument is set to similarity_scores.get to specify that
the maximum should be determined based on the values of the dictionary. 
The movie title with the highest similarity score is then returned as 
the result of the function'''
similar_movie = find_similar_movie(description)
print("Recommended movie for you based on your viewing history is :", similar_movie)


# answer 
# Recommended movie for you based on your viewing history is : Movie C
'''A darkness swirls at the center of a world-renowned dance company, 
one that will engulf the artistic director, an ambitious young dancer, 
and a grieving psychotherapist. 
Some will succumb to the nightmare. Others will finally wake up.'''