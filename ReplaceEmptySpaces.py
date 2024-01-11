import os

def replace_spaces_with_underscore(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.html') and ' ' in file:
                old_path = os.path.join(root, file)
                new_file = file.replace(' ', '_')
                new_path = os.path.join(root, new_file)

                if old_path != new_path:
                    os.rename(old_path, new_path)
                    print(f'Renamed: {file} in {root} to {new_file}')

if __name__ == "__main__":
    current_folder = os.path.join(os.getcwd(), 'C:\\Users\\Usuario\\Documents\\GitHub\\EmailScrapper\\archived')  # Adjust this path accordingly
    replace_spaces_with_underscore(current_folder)
