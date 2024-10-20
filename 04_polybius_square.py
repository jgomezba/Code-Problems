import string

def split_list(lst:list, n:int) -> list:
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def get_matrix_from_alphabet() -> list:
    english_alphabet = list(string.ascii_uppercase)
    start_index = english_alphabet.index('I') 
    end_index = english_alphabet.index('J')   

    english_alphabet[start_index:end_index + 1] = ['I/J']
    
    return split_list(english_alphabet, 5)

def decode_from_numbers(matrix:list, numbers:str) -> str:
    final_decoder = ""
    
    for pair in split_list(list(numbers), 2):
        row_index = int(pair[0]) - 1
        column_index = int(pair[1]) - 1
        
        letter = matrix[row_index][column_index]
        if letter == "I/J":
            letter = "I"
        
        final_decoder += letter
        
    return final_decoder

def decode_from_text(matrix:list, text:str) -> str:
    final_decoder = ""
    
    for letter in text:
        letter = letter.upper()
        row_ident = 0
        for row in matrix:
            result = row.index(letter) if letter in row else (row.index("I/J") if ((letter == "I" or letter == "J") and "I/J" in row) else -1) 
            if result >= 0:
                final_decoder += str(row_ident+1) + str(result+1)
                break
            else:   
                row_ident += 1
    
    return final_decoder
        

def decode_text(matrix:list, text:str) -> str:
    if text.isdigit():
        return decode_from_numbers(matrix, text)
    else:
        return decode_from_text(matrix, text)

if __name__ == "__main__":
    polybius_matrix = get_matrix_from_alphabet()
    print(decode_text(polybius_matrix, "2311424254"))
