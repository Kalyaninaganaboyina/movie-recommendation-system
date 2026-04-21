import pandas as pd
movies=pd.read_csv(r"C:\python\movie_recomandation_system\tmdb_5000_movies.csv",low_memory=False)
credits_=pd.read_csv(r"C:\python\movie_recomandation_system\tmdb_5000_credits.csv",low_memory=False)
movies=movies.merge(credits_,on="title")
movies=movies[["movie_id","title","overview","genres","keywords","cast","crew"]]
movies.dropna(inplace= True)
#print(movies.head())
#print(movies.shape)
#for converting strings attributes into list
import ast
def convert(text):
     L=[]
     try:
       for i in ast.literal_eval(text):
          L.append(i["name"])
     except:
       return []
     return L
movies["genres"]=movies["genres"].apply(convert)
movies["keywords"]=movies["keywords"].apply(convert)
movies["cast"]=movies["cast"].apply(convert)
movies["crew"]=movies["crew"].apply(convert)
#print(movies["cast"])
###
movies["genres"]=movies["genres"].apply(lambda x: " ".join(x))
movies['keywords']=movies['keywords'].apply(lambda x: " ".join(x))
movies["cast"]=movies["cast"].apply(lambda x: " ".join(x))
movies["crew"]=movies["crew"].apply(lambda x: " ".join(x))
movies["cast"]=movies["cast"].apply(lambda x: x.replace(" ",""))
movies["crew"]=movies["crew"].apply(lambda x: x.replace(" ",""))
movies["tags"]=movies["overview"]+" "+movies["genres"]+" "+movies["keywords"]+" "+movies["cast"]+" "+movies["crew"]
movies["tags"]=movies["tags"].apply(lambda x: x.lower())
#print(movies["tags"])
######
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cv=CountVectorizer(max_features=5000,stop_words="english")
vectors=cv.fit_transform(movies["tags"]).toarray()
similarity= cosine_similarity(vectors)
###
movies["title_lower"]=movies["title"].str.lower()
def recommend():
     movie=input("Hello,Enter your movie name: ").lower()
     if movie not in movies["title_lower"].values:
          print(" Movie not found, please,try again!")
          return
     index=movies[movies['title_lower']==movie].index[0]
     distance=similarity[index]
     movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]
     print("\n\nRecommended movies:")
     for i,m in enumerate(movies_list):
          print(f"{i+1}) {movies.iloc[m[0]].title}")
     print("enjoy yours movies..!\n")
while True:
    recommend()
    while True:
       again=input("Do you wnat another recommendation? (Yes/No):")
       if  again.lower() =="no":
         print("Thanking you for using movie recommendation system..!")
         print("Have a nice day>>>")
         exit()
       elif again.lower() =="yes":
         break
       else:
         print("Invalid input! Please enter only yes or no")
import pickle
pickle.dump(open("movie_recommendation.pkl","wb"))
       
     
