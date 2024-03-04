import os
import markdown
from datetime import datetime

def extract_heading_and_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        html_content = markdown.markdown(content)
        # Assuming the first h1 tag is the main heading
        heading = html_content.split('<h1>', 1)[-1].split('</h1>', 1)[0]
        return heading.strip(), content.strip()

def process_folder(folder_path, existing_dict=None):
    if existing_dict is None:
        existing_dict = {}

    try:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.md'):
                file_path = os.path.join(folder_path, file_name)
                heading, content = extract_heading_and_content(file_path)
                existing_dict[heading] = content
    except FileNotFoundError:
        print(f"Folder not found at location: {folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return existing_dict

def save_dict_to_md(dictionary, output_folder):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(output_folder, f"output_{timestamp}.md")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("# Dictionary Output\n\n")
        for heading, content in dictionary.items():
            file.write(f"## {heading}\n\n```markdown\n{content}\n```\n\n")

    return output_file

# Example usage
folder_location = '/home/navin/arjo_llm/Arjo Ai'
output_folder = '/home/navin/arjo_llm/output_md_files'

result_dict = process_folder(folder_location)

# Save the dictionary to a new MD file with a timestamp
saved_file = save_dict_to_md(result_dict, output_folder)

print(f"Data saved to {saved_file}")