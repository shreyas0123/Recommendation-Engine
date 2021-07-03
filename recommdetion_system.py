######################### problem1 ######################
import pandas as pd
#load the dataset
game = pd.read_csv("C://Users//DELL//Downloads//game.csv",encoding = 'utf8')
game.shape
game.columns

from sklearn.feature_extraction.text import TfidfVectorizer
#creating a Tfidf Vetorizer to remove all stop words
tfidf = TfidfVectorizer(stop_words = "english")

# replacing the NaN values in overview column with empty string
game["game"].isnull().sum() 
game["game"] = game["game"].fillna(" ")

#preparing the Tfidf matrix by fitting and transforming
tfidf_matrix = tfidf.fit_transform(game.game)
tfidf_matrix.shape

from sklearn.metrics.pairwise import linear_kernel
#computing the cosine similarity on Tfidf matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
#creating a mapping of game name to index number
game_index = pd.Series(game.index, index = game['game']).drop_duplicates()
game_index = game_index[~game_index.index.duplicated(keep = 'first')]

game_id = game_index["SoulCalibur"]
game_id

def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the game index using its title 
    game_id = game_index[Name]
    
    # Getting the pair wise similarity score for all the game's with that 
    # game
    cosine_scores = list(enumerate(cosine_sim_matrix[game_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN+1]
    
    # Getting the game index 
    game_idx  =  [i[0] for i in cosine_scores_N]
    game_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar movies and scores
    game_similar_show = pd.DataFrame(columns=["name", "Score"])
    game_similar_show["name"] = game.iloc[game_idx,1]
    game_similar_show["Score"] = game_scores
    game_similar_show.reset_index(inplace = True)  
    print (game_similar_show)
    
# Enter your anime and number of anime's to be recommended 
get_recommendations("Metal Gear Solid 2: Sons of Liberty", topN = 10)
game_index["Metal Gear Solid 2: Sons of Liberty"]

############################### problem2 ############################
import pandas as pd

# import Dataset 
entertainment = pd.read_csv("C:\\Users\\DELL\\Downloads\\Entertainment.csv", encoding = 'utf8')
entertainment.shape # shape
entertainment.columns

from sklearn.feature_extraction.text import TfidfVectorizer 
# Creating a Tfidf Vectorizer to remove all stop words
tfidf = TfidfVectorizer(stop_words = "english")    
# replacing the NaN values in overview column with empty string
entertainment["Category"].isnull().sum() 
entertainment["Category"] = entertainment["Category"].fillna(" ")

# Preparing the Tfidf matrix by fitting and transforming
tfidf_matrix = tfidf.fit_transform(entertainment.Category)   #Transform a count matrix to a normalized tf or tf-idf representation
tfidf_matrix.shape 

from sklearn.metrics.pairwise import linear_kernel

# Computing the cosine similarity on Tfidf matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# creating a mapping of entertainment name to index number 
entertainment_index = pd.Series(entertainment.index, index = entertainment['Titles']).drop_duplicates()

entertainment_id = entertainment_index["Jumanji (1995)"]
entertainment_id

def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the entertainment  index using its title 
    entertainment_id = entertainment_index[Name]
    
    # Getting the pair wise similarity score for all the anime's with that 
    # anime
    cosine_scores = list(enumerate(cosine_sim_matrix[entertainment_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN+1]
    
    # Getting the movie index 
    entertainment_idx  =  [i[0] for i in cosine_scores_N]
    entertainment_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar movies and scores
    entertainment_similar_show = pd.DataFrame(columns=["name", "Score"])
    entertainment_similar_show["name"] = entertainment.loc[entertainment_idx, "Titles"]
    entertainment_similar_show["Score"] = entertainment_scores
    entertainment_similar_show.reset_index(inplace = True)  
    # anime_similar_show.drop(["index"], axis=1, inplace=True)
    print (entertainment_similar_show)
    # return (entertainment_similar_show)

    
# Enter your entertainment and number of entertainment's to be recommended 
get_recommendations("How to Make an American Quilt (1995)", topN = 10)
entertainment_index["How to Make an American Quilt (1995)"]


















    