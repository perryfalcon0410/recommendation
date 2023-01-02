import sys
import pymongo
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://perry:runningman7012@e-commerce.yx9dq1w.mongodb.net/?retryWrites=true&w=majority&authSource=admin")
db = client.petstore
products=db['products']
df = pd.DataFrame(list(products.find()))
#print(df['description'])

tfidf=TfidfVectorizer(stop_words="english")
df['description']=df['description'].fillna("")
tfidf_matrix=tfidf.fit_transform(df['description'])

cosine_sim=linear_kernel(tfidf_matrix, tfidf_matrix)

indices=pd.Series(df.index,index=df['_id']).drop_duplicates()

def get_recommendations(name,cosine_sim=cosine_sim):
    idx=indices[name]
    sim_scores=enumerate(cosine_sim[idx])
    sim_scores=sorted(sim_scores,key=lambda x: x[1],reverse=True)
    sim_scores=sim_scores[1:5]
    sim_index=[i[0] for i in sim_scores]
    result=[df['_id'].iloc[i] for i in sim_index]
    return result
  


