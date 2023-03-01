import os
from google.cloud import storage


#Creating an environmental variable for the service key configuration
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

#Creating a storage unit
storage_client = storage.Client()


# List the class methods
# print(dir(storage_client))

#Creating a new bucket
bucket_name = 'movies_etl_bucket01'
bucket = storage_client.bucket(bucket_name=bucket_name)
bucket.location = 'US'
#bucket = storage_client.create_bucket(bucket)

#Access the bucket
my_bucket = storage_client.get_bucket('movies_etl_bucket01')

#print the details
#print(vars(bucket))

def upload_data_to_bucket(blob_name,file_path,bucket_name):
    try:
        
        #access the bucket
        bucket = storage_client.get_bucket(bucket_name)

        #create a blob(instance) from the bucket

        blob = bucket.blob(blob_name=blob_name)


        #updload file
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False
#specify the file path
movie_path = 'movies.csv'
ratings_path = 'ratings.csv'


#upload csv files to Bucket
upload_data_to_bucket(blob_name='first_project/movies',file_path=movie_path,bucket_name='movies_etl_bucket01')
upload_data_to_bucket(blob_name='first_project/ratings',file_path=movie_path,bucket_name='movies_etl_bucket01')
