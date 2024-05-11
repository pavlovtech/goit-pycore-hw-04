import sys
import os
from pathlib import Path
from colorama import init, Fore

# Initialize Colorama
init()

def visualize_directory_structure(path, level=0, prefix=''):
    try:
        base_path = Path(path)
        if not base_path.is_dir():
            print(Fore.RED + "The provided path is not a directory.")
            return
    except Exception as e:
        print(Fore.RED + f"Error accessing path: {e}")
        return
    
    # Get all entries in the directory sorted by name
    for entry in sorted(base_path.iterdir(), key=lambda x: x.name):

        indent = '    ' * level
        # Print directories in one color and files in another
        if entry.is_dir():
            print(Fore.BLUE + f"{prefix}{indent}{entry.name}/")
            
            # Recursive call for the next level of the directory
            visualize_directory_structure(entry, level + 1, prefix + indent)
        elif entry.is_file():
            print(Fore.GREEN + f"{prefix}{indent}{entry.name}")

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python hw03.py <path_to_directory>")
    else:
        visualize_directory_structure(sys.argv[1])