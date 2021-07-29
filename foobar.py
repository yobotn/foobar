def solution(s):
    alphabet = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    braille_codes = [
                    '000000',
                    '100000',
                    '110000',
                    '100100',
                    '100110',
                    '100010',
                    '110100',
                    '110110',
                    '110010',
                    '010100',
                    '010110',
                    '101000',
                    '111000',
                    '101100',
                    '101110',
                    '101010',
                    '111100',
                    '111110',
                    '111010',
                    '011100',
                    '011110',
                    '101001',
                    '111001',
                    '010111',
                    '101101',
                    '101111',
                    '101011']


    binary_response = ''

    for letter in s:

      idx = alphabet.index(letter.lower())

      if letter.isupper():
        binary_response += '000001'

      binary_response += braille_codes[idx]


    return binary_response


print(solution('abc'))