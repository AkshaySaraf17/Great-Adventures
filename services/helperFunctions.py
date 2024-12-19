def extract_text_after_choice1(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Find the index of '1.' and the next full stop '.'
        start_index = content.find('1.') + len('1.')
        end_index = content.find('.', start_index)

        # Extract the text between '1.' and the next full stop '.'
        extracted_text = content[start_index:end_index].strip()
        return extracted_text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def extract_text_after_choice2(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Find the index of '1.' and the next full stop '.'
        start_index = content.find('2.') + len('2.')
        end_index = content.find('.', start_index)

        # Extract the text between '1.' and the next full stop '.'
        extracted_text = content[start_index:end_index].strip()
        return extracted_text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def extract_text_after_choice3(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Find the index of '1.' and the next full stop '.'
        start_index = content.find('3.') + len('3.')
        end_index = content.find('.', start_index)

        # Extract the text between '1.' and the next full stop '.'
        extracted_text = content[start_index:end_index].strip()
        return extracted_text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def read_intro_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Extract the first sentence
        sentences = content.split('?')
        first_sentence = sentences[0].strip()

        return first_sentence
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None



