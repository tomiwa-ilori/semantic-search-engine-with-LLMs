## Search AI with OpenAI Embeddings
This is a web application that allows users to perform semantic search using OpenAI embeddings. It uses the OpenAI API to generate embeddings for text data and calculates the similarity between the user's search query and each row of a provided dataset. The application then returns the top matching results based on the similarity score.

## Getting Started
To run the application, follow these steps:
1. Install the required libraries by running pip install -r requirements.txt.
2. Set up your OpenAI API key. You can either set it as an environment variable or enter it directly in the application.
3. Make sure you have a dataset in CSV format. The application expects the dataset to have a column named "ada_embeddings" containing the embeddings for each row.
4. Run the app.py file using streamlit run app.py.

Access the application in your web browser.

## Usage
Enter your OpenAI API key in the provided text input field.
Enter your search query in the search query text input field.
Click the "Search" button to perform the search.
The application will display the top matching results from the dataset, along with their similarity scores.

## Customization
You can customize the application by modifying the following:

1. The text embedding model used for generating embeddings. Currently set to 'text-embedding-ada-002', but you can change it to a different model.
2. The number of results to display. Currently set to 4, but you can adjust it as needed.
3. The dataset file path. Currently set to "data/University_reviews.csv", but you can change it to your own dataset.

## Acknowledgements
This application was developed using the OpenAI API and the Streamlit library. Special thanks to the developers of these tools for making this project possible.
