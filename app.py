
# Import the required libraries
import openai
import numpy as np
import pandas as pd
import streamlit as st
from tqdm import tqdm
tqdm.pandas()
from openai.embeddings_utils import get_embedding, cosine_similarity

# Load the API key from an environment variable or secret management service

#openai.api_key = os.getenv("OPENAI_API_KEY")

# Set Title of the Web App
st.title("Search AI with OpenAI Embeddings")

# Request the user to enter their API key
user_secret = st.text_input(label = ":green[OpenAI API Key]", 
                            placeholder = "Enter your OpenAI API Key Here", 
                            type="password")

if user_secret:
    openai.api_key = user_secret

# Define a function to load the data
@st.cache_data
def load_data():
    df = pd.read_csv("data/University_reviews.csv")
    return df

def search(query, df, n=4, pprint=True):

    # Select embedding to use for the query
    text_embedding_model = 'text-embedding-ada-002'

    # Convert the embedding of the query to a numpy array
    df['ada_embeddings'] = df.ada_embeddings.apply(eval).apply(np.array)

    # Get the embedding for the query
    query_embedding = get_embedding(query, engine=text_embedding_model)

    # Calculate the similarity between the query and each row of the dataframe
    df['similarity'] = df.ada_embeddings.progress_apply(lambda x: cosine_similarity(x, query_embedding))

    # Sort the dataframe by similarity and return the top n results
    output = (df.sort_values(by='similarity', ascending=False).head(n))

    if pprint:
        print(output)
    return output

# Request the user to enter their search query
query = st.text_input(label = ":green[Search Query]", 
                            placeholder = "Enter your search query here", 
                            type="default")

# Create a button to run the search
query_button = st.button(label = "Search", type="primary")

# Validate that the user has entered a search query
if query:
    # Validate that the user has clicked the search button
    if query_button:
        # Load the data
        df = load_data()
        # Run the search
        result = search(query, df, 4, True)
        # Display the results and the similarity score
        for index, row in result.iterrows():
            st.write(row["similarity"], row["University"])