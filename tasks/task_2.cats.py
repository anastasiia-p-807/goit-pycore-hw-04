
def get_cats_info(path: str) -> list:
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as cats_data_file:
            for cat in cats_data_file:
                cat = cat.strip()
                if cat:
                    id, name, age = cat.split(',')
                    cats_info.append({"id": id, "name": name, "age": age})
    except Exception as e:
        print(f"Error reading file: {e}")

    return cats_info

cats_info = get_cats_info("tasks/test_data/cats.txt")
print(cats_info)
