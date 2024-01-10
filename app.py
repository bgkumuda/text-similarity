# Import required modules from Flask framework
from flask import Flask, request, jsonify
import string

# Initialize a Flask application
app = Flask(__name__)


# Function to preprocess a text by converting it to lowercase, removing punctuation, and creating a set of tokens
def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove punctuation from the text using translation table
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split the text into tokens and create a set of unique tokens
    tokens = text.split()
    return set(tokens)


# Function to calculate Jaccard similarity between two texts
def calculate_jaccard_similarity(text1, text2):
    # Preprocess the texts to obtain sets of tokens
    set1 = preprocess_text(text1)
    set2 = preprocess_text(text2)

    # Calculate the intersection and union of the token sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Calculate Jaccard similarity as the ratio of intersection to union size
    similarity = len(intersection) / len(union)
    return similarity


# Define a route for comparing two texts using Jaccard similarity
@app.route('/compare_texts', methods=['POST'])
def compare_texts():
    try:
        # Retrieve JSON data from the request
        data = request.get_json()
        text1 = data['text1']
        text2 = data['text2']

        # Calculate Jaccard similarity between the provided texts
        similarity = calculate_jaccard_similarity(text1, text2)

        # Prepare a response with similarity value and success message
        response = {
            'similarity': similarity,
            'message': 'Texts comparison successful.'
        }

        # Return the response as JSON with HTTP status code 200 (OK)
        return jsonify(response), 200

    except Exception as e:
        # Handle exceptions and return an error response with HTTP status code 500 (Internal Server Error)
        error_message = f"Error: {str(e)}"
        return jsonify({'error': error_message}), 500


# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
