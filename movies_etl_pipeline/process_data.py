import pandas as pd
import numpy as np 
from os import read


#create a dataframe for movies names
ratings =pd.read_csv('ml-100k/u.data', delimiter='\t', header=None, names=['user_id','item_id','rating','timestamp'])

# Create a dataframe for Movie Names
with open('ml-100k/u.item','r',encoding='ISO-8859-1') as read_file:
    
    counter = 0
    movies_df =pd.DataFrame(columns=['item_id','movie_name','release_timestamp'])

    #iterate through the lines in the file
    for line in read_file:
        
        #for each line extract the first three values
        fields = line.split('|')
        item_id,movie_name,release_timestamp = fields[0],fields[1],fields[2]
        movie_name = movie_name[0:len(movie_name) - len(' (1234)')]

        #aggregate line data
        line_data = [int(item_id),str(movie_name),release_timestamp]


        #creating a temporary table and concat it with the movies_df
        temp_df = pd.DataFrame(data=[line_data],columns=['item_id','movie_name','release_timestamp'])
        movies_df = pd.concat([temp_df,movies_df],ignore_index=True)

        counter +=1
    #sort the values by item_id
    movies_df.sort_values(by='item_id',ascending=True,inplace=True)
#close file
read_file.close()

#export to csv
ratings.to_csv('ratings.csv',index=False)
movies_df.to_csv('movies.csv',index=False)

