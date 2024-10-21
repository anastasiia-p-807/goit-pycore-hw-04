import sys
from pathlib import Path
from colorama import init, Fore, Style

def visualize_directory_structure(directory_path: str, level: int = 0) -> None:
    try:
        path = Path(directory_path)
        if not path.exists():
            print(Fore.RED + f"Path does not exist: {directory_path}" + Style.RESET_ALL)
            return
        if not path.is_dir():
            print(Fore.RED + f"Path is not a directory: {directory_path}" + Style.RESET_ALL)
            return

        for item in path.iterdir():
            indent = ' ' * 4 * level
            if item.is_dir():
                print(Fore.LIGHTYELLOW_EX + f"{indent}{item.name}/" + Style.RESET_ALL)
                
                # skipping .git and .venv folders because there are too many files
                if item.name not in [".git", ".venv"]:    
                    visualize_directory_structure(item, level + 1)
            else:
                print(Fore.WHITE + f"{indent}{item.name}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    init(autoreset=True)

    directory = sys.argv[1]
    visualize_directory_structure(directory)
