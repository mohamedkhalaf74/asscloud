import os
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Download NLTK stopwords
nltk.download('stopwords')

def read_file(file_path):
    """Read the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def preprocess_text(text):
    """Preprocess text by removing stopwords and non-alphabetic characters."""
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())  # Tokenize words
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_word_frequency(words):
    """Count the frequency of each word."""
    return Counter(words)

def display_word_frequency(word_counts):
    """Display the word frequency count."""
    for word, count in word_counts.items():
        print(f'{word}: {count}')

def main():
    file_path = os.path.join("C:", "Users", "shiko", "Desktop", "random_paragraphs.txt")
    contents = read_file(file_path)
    if contents:
        print("Original text:")
        print(contents)
        
        print("\nText with stopwords removed:")
        processed_text = preprocess_text(contents)
        print(processed_text)

        print("\nWord frequency count:")
        word_counts = count_word_frequency(processed_text)
        display_word_frequency(word_counts)

if __name__ == "__main__":
    main()
