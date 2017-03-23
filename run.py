import json
from pprint import pprint


#Constants here
TOTAL_ITEMS = 250

WEIGHT_GENRE = 95
WEIGHT_DIRECTOR = 29
WEIGHT_STAR = 15
WEIGHT_FACTOR_RATING = 2.5  # A difference of one in rating will cause shift of 2.5 in score

KEY_RATING = 'rating'
KEY_GENRE =  'genre'
KEY_STARS = 'stars'
KEY_DIRECTOR = 'director'
KEY_ID = 'movie_id'
KEY_DESCRIPTION = 'description'
KEY_TITLE = 'title'


def calculate_score(moviedata, refIndex):
    baseMovie = moviedata[refIndex]
    
    scores=[]
    for i in range(TOTAL_ITEMS):
        movie = moviedata[i]
        
        scores.insert(i, [movie[KEY_ID], movie[KEY_TITLE], 0])
        score = 0           #This is a temp var, will be eventually assigned to scores list
        
        if (i==refIndex):
            continue
        
        #Start calculating the score
        
        #Matching genre
        baseGenres = baseMovie[KEY_GENRE]
        genres = movie[KEY_GENRE]
        
        for genre in genres:
            for baseGenre in baseGenres:
                if(baseGenre == genre):
                    score += WEIGHT_GENRE
            
        #Matching stars
        baseStars = baseMovie[KEY_STARS]
        stars = movie[KEY_STARS]
        
        for star in stars:
            for baseStar in baseStars:
                if(baseStar == star):
                    score += WEIGHT_STAR
                    
        #Matching directors
        baseDirectors = baseMovie[KEY_DIRECTOR]
        directors = movie[KEY_DIRECTOR]
        
        for director in directors:
            for baseDirector in baseDirectors:
                if(baseDirector == director):
                    score += WEIGHT_DIRECTOR
                    
        #Calculating final deflection due to rating (small effect only)
        rating = movie[KEY_RATING]
        score += float(rating) * WEIGHT_FACTOR_RATING

        #Assigning score to the scores list
        scores[i][2] = score
        
        
    return scores


with open('input.json') as json_file:    
    data = json.load(json_file)

finalData = {}

for i in range(TOTAL_ITEMS):
    movieScoreList = calculate_score(data, 0)
    sorted(movieScoreList, key=lambda movieScoreListItem: -movieScoreListItem[2])
    
    for i in range(10):
        print scores[i][1]




