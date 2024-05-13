filename = "test.txt"
content = ""

# -------
def get_value_from_txt(filename):
  try:
    with open(filename, 'r') as file:
      value = file.readline().strip()
      return value
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    return None
# -------

value = get_value_from_txt(filename)

# -------
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file '{filename}': {e}")
# -------

if value == "":
    print("Looks like you are first time here.\nPlease, set download path, so I will know where to download files to.")
    content = input("\nSet download path: ")
    write_to_file(filename, content)
    print(f"inside IF = {get_value_from_txt(filename)}")

print(f"outside IF = {get_value_from_txt(filename)}")

# print("Download path set to:", value)


# print(f"Content written to file: {filename}")
