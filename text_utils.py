import re

def get_cleaned_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower().strip()
    # remove extra spaces
    formatted_text = ' '.join(cleaned_text.split())
    return formatted_text

def read_file(file_name, clean=True):
    """
    if clean param is True, it will return cleaned text (like removing punctuations, etc.)
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        if clean:
            return get_cleaned_text(file.read())
        return file.read()

if __name__ == '__main__':
    print(read_file('test.txt', clean=True))
