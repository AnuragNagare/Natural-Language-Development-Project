import argparse
import random
import spacy
import os

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Step 1: Parsing Command-Line Arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Check word length and generate phrases.")
    parser.add_argument("file_path", type=str, help="Path to the input text file.")
    parser.add_argument("min_length", type=int, help="Minimum character length.")
    parser.add_argument("max_length", type=int, help="Maximum character length.")
    return parser.parse_args()

# Step 2: Checking the Character Range
def is_within_range(word, min_length, max_length):
    return min_length <= len(word) <= max_length

# Step 3: Generating the Phrase using spaCy
def generate_phrase(word):
    # Create a simple sentence with the word
    doc = nlp(word)
    # Generate a phrase using spaCy's linguistic annotations
    phrase = f"The {word} is {random.choice(['red', 'green', 'blue', 'yellow', 'orange'])}"
    return phrase

def process_text_file(file_path, min_length, max_length):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)  # Go back to the beginning of the file

        for line in lines:
            words = line.strip().split()
            processed_line = []

            for word in words:
                if is_within_range(word, min_length, max_length):
                    phrase = generate_phrase(word)
                    processed_line.append(phrase)
                else:
                    processed_line.append(word)

            file.write(' '.join(processed_line) + '\n')
        
        file.truncate()  # In case the new content is shorter than the old

def main():
    args = parse_arguments()
    
    file_path = args.file_path
    min_length = args.min_length
    max_length = args.max_length
    
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return
    
    process_text_file(file_path, min_length, max_length)
    print(f"Processing complete. Phrases have been generated and saved in '{file_path}'.")

if __name__ == "__main__":
    main()
