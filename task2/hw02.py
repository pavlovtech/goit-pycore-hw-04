def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(',')

                    # Construct a dictionary with the cat information
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }

                    # Append the dictionary to the list of cats
                    cats.append(cat_info)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return cats

cats_info = get_cats_info("task2/cats_file.txt")
print(cats_info)