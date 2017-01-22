#!/usr/bin/python

from libs.ask import alexa
from libs.canistreamit import search, streaming

search_results = search("John Carpenter's Vampires")
#print(search_results[0]) #title

print("Found " + str(len(search_results)) + " results.")

for i in range(len(search_results)):
    #print(search_results[i]['title'])
    #print(search_results[i]['affiliates'])
    movie = search_results[i]
    print(movie['title'])
    print(movie['affiliates']['amazon_prime_instant_video'])
    print(movie['affiliates']['netflix_instant'])
    print("===========================")
