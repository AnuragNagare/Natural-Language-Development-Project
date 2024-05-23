# Natural-Language-Development-Project

# ReadMe: Explanation of the Word Length Checker and Phrase Generator

## Overview
This Python script reads a text file, checks if words fall within a specified character length range, and replaces those words with generated phrases. It utilizes command-line arguments for input parameters, the spaCy library for natural language processing, and basic file I/O operations.

## Components

### 1. Command-Line Arguments Parsing
The script uses the `argparse` module to handle command-line arguments. These arguments include:
- `file_path`: The path to the input text file.
- `min_length`: The minimum character length of words to be processed.
- `max_length`: The maximum character length of words to be processed.

### 2. Checking Character Range
The function `is_within_range(word, min_length, max_length)` verifies if a word's length falls within the specified minimum and maximum character limits.

### 3. Phrase Generation
The `generate_phrase(word)` function creates a simple phrase using the given word. It uses the spaCy library to process the word and appends a random color to generate a descriptive phrase.

### 4. Text File Processing
The `process_text_file(file_path, min_length, max_length)` function:
- Opens the specified text file for reading and writing.
- Reads each line of the file and splits it into words.
- Checks each word against the character length criteria.
- If a word meets the criteria, it is replaced with a generated phrase.
- Writes the processed lines back to the file.
- Truncates the file to ensure no residual content from the previous version remains.

### 5. Main Function
The `main()` function:
- Parses the command-line arguments.
- Checks if the specified file exists.
- Calls the `process_text_file` function to process the file.
- Outputs a message indicating completion.

### Error Handling
The script includes basic error handling to check if the specified file exists and provides an error message if it does not.

## Usage
To run the script, use the following command:
```
python script_name.py <file_path> <min_length> <max_length>
```
Replace `<file_path>` with the path to your text file, `<min_length>` with the minimum word length, and `<max_length>` with the maximum word length.

### Example
```
python script.py input.txt 4 7
```
This example processes the file `input.txt`, replacing words with a length between 4 and 7 characters with generated phrases.

## Dependencies
- `argparse`: For parsing command-line arguments.
- `spacy`: For natural language processing (specifically, the English language model `en_core_web_sm`).
- `random`: For generating random phrases.
- `os`: For file path operations.

Make sure to install the spaCy library and download the English model before running the script:
```
pip install spacy
python -m spacy download en_core_web_sm
```
