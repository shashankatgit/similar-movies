import json
from RAKE import rake


#Constants here
TOTAL_ITEMS = 250

#Weights of different parameters for calculating similarity

WEIGHT_GENRE = 95
WEIGHT_DIRECTOR = 15
WEIGHT_STAR = 10
WEIGHT_FACTOR_RATING = 2.5  # A difference of one in rating will cause shift of 2.5 in score

#JSON keys in the input

KEY_RATING = 'rating'
KEY_GENRE =  'genre'
KEY_STARS = 'stars'
KEY_DIRECTOR = 'director'
KEY_ID = 'movie_id'
KEY_DESCRIPTION = 'description'
KEY_TITLE = 'title'


def calculate_score(moviedata, refIndex):
    baseMovie = moviedata[refIndex]
    
    ##Experimental feature - Rapid Automatic Keyword Extraction - Part 1
    
    scores=[]
    for i in range(TOTAL_ITEMS):
        movie = moviedata[i]
        
        scores.insert(i, [movie[KEY_ID], movie[KEY_TITLE], 0])
        score = 0           #This is a temp var, will be eventually assigned to scores list
        
        if (i==refIndex):
            continue        #Comparison with ownself case
        
        #Start calculating the score
        
        #Matching genre
        baseGenres = baseMovie[KEY_GENRE]
        genres = movie[KEY_GENRE]
        
        for genre in genres:
            for baseGenre in baseGenres:
                if(baseGenre == genre):
                    ##print 'genre match : '+genre
                    score += WEIGHT_GENRE
            
        #Matching stars
        baseStars = baseMovie[KEY_STARS]
        stars = movie[KEY_STARS]
        
        for star in stars:
            for baseStar in baseStars:
                if(baseStar == star):
                    ##print 'star match : '+star
                    score += WEIGHT_STAR
                    
        #Matching directors
        baseDirector = baseMovie[KEY_DIRECTOR]
        director = movie[KEY_DIRECTOR]
        
        if(baseDirector == director):
            ##print 'director match : '+director
            score += WEIGHT_DIRECTOR
                    
        #Calculating final deflection due to rating (small effect only)
        rating = movie[KEY_RATING]
        score += float(rating) * WEIGHT_FACTOR_RATING

        #Assigning score to the scores list
        scores[i][2] = score
        
        ## Experimental feature - Rapid Automatic Keyword Extraction - Part2
        
        
    return scores


# Control begins from here
with open('input.json') as json_file:    
    data = json.load(json_file)



finalData = {}

for i in range(TOTAL_ITEMS):
    baseMovieTitle = data[i][KEY_TITLE]
    movieScoreList = calculate_score(data, i)
    sortedMovieScoreList = sorted(movieScoreList, key=lambda movieScoreListItem: -movieScoreListItem[2])
    
    tempArray = [];
    for i in range(10):
        tempArray.insert(i, sortedMovieScoreList[i][1])
        
    #Storing only name of the movie in JSON
    finalData[baseMovieTitle] = tempArray


with open('output.json','w') as outfile:
    json.dump(finalData, outfile)


