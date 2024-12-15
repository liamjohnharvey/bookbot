def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = count_words(text)
    character_count = count_characters(text)
    character_list = convert_dict(character_count)
    generate_report(book, word_count, character_list)

def get_text(path):
        with open(path) as f:
            return f.read()

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1

    return count

def count_characters(text):
    character_string = list(text.lower())
    character_count = {}
    
    for character in character_string:
        if character in character_count:
               character_count[character] += 1
        else:
             character_count[character] = 1
 
    return character_count 

def convert_dict(dict):
    character_list = []
    for character in dict:
         character_list.append({"name": character, "num": dict[character]})
         
    return character_list
     
          

def sort_on(dict):
    return dict["num"]

def generate_report(book, word_count, character_list):
    character_list.sort(reverse=True, key=sort_on) 

    print("--- Begin report of " + book + " ---")
    print(f"{word_count} words found in the document")
    print("")
    for character in character_list:
        if character["name"].isalpha():
            print(f"The {character["name"]} character was found {character["num"]} times")
    print("--- End report ---")
     
     

main()