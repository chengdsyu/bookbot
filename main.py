def main ():
  path_of_file = "books/frankenstein.txt"
  text = read_file(path_of_file)
  word_count = count_words(text)
  character_count = count_characters(text)
  sorted_report = sort_report(character_count)

  print(f"--- Begin report of {path_of_file} ---")
  print(f"{word_count} words found in the document")
  print()

  for letter in sorted_report:
      if not letter["char"].isalpha():
          continue
      print(f"The '{letter['char']}' character was found {letter['number']} times")

  print("--- End report ---")


def read_file(path):
  with open(path) as f:
    return f.read()
  
def count_words(word):
  words = word.split()
  return len(words)

def count_characters(character):
  character_dict = {}
  for c in character:
    lowercase_c = c.lower()
    if lowercase_c in character_dict:
      character_dict[lowercase_c] += 1
    else:
      character_dict[lowercase_c] = 1
  return character_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["number"]

def sort_report(dictionary):
  sorted_list = []
  # letter accesses the KEY in the dictionary
  for letter in dictionary:
    # dictinary[letter] accesses the value in the dictionary
    sorted_list.append({"char": letter, "number": dictionary[letter]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

main()