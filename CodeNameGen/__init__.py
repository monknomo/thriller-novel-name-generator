from wordnik import *
from wordnik.models import WordObject
from random import shuffle
import config


"""
Prints two random words, an adjective and a noun, from the Wordnik API
http://developer.wordnik.com/


Requires that you have a config.py accessible, and that config.py contains the
variable "apiKey" which is a string that is a valid Wordnik API key


Examples:


    $ python codeNameGen.py
    Emergent Nativity


Attributes:
    apiUrl (str): The Wordnik API base url
    client (wordnik.swagger.ApiClient): The Wordnik API Swagger generated
        client
    wordsApi (str): The Wordnik Words API
    minCorpusCount(int): The minimum number of occurences in the corpus
    minDictionaryCount(int): The minimum number dictionary occurences
    minLength(int): The minimum length of the word
    maxLength(int): The maximum length of the word
    limit(int): The maximum number of words to return
"""


apiUrl = 'http://api.wordnik.com/v4'
client = swagger.ApiClient(config.apiKey, apiUrl)


wordsApi = WordsApi.WordsApi(client)
minCorpusCount = 50
minDictionaryCount = 20
minLength = 3
maxLength = 12
limit = 1


"""
Returns two title-cased random words separated by a space, an adjective and a
noun, from the Wordnik API: http://developer.wordnik.com/


Returns:
    String consisting of two title-case random words, an adjective and a noun
"""

def get_code_name():
    adjective = wordsApi.getRandomWord(includePartOfSpeech="adjective",
                                       minCorpusCount=minCorpusCount,
                                       minDictionaryCount=minDictionaryCount,
                                       minLength=minLength,
                                       maxLength=maxLength)
    noun = wordsApi.getRandomWord(includePartOfSpeech="noun",
                                  minCorpusCount=minCorpusCount,
                                  minDictionaryCount=minDictionaryCount,
                                  minLength=minLength,
                                  maxLength=maxLength)
    return (adjective.word + " " + noun.word).title()

if __name__ == "__main__":
    print(get_code_name())