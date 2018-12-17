"""Morse code encoding and decoding

Author: Beka Beriashvili
"""
#!/usr/bin/env python3
# encoding: UTF-8


from notes.trees.BinaryTree import BinaryTree


class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        """Constructor"""
        self.morse_tree = BinaryTree('')

        with open(file_in) as morseF:
            for i in morseF:
                letter, code = i.split()
                self.follow_and_insert(code, letter)


    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""
        treeM = self.morse_tree
        for i in code_str:            
            if i == '.':
                if treeM.get_child_left() == None:
                    treeM.insert_left('')
                treeM = treeM.get_child_left()
            else:
                if treeM.get_child_right() == None:
                    treeM.insert_right('')
                treeM = treeM.get_child_right()
        treeM.set_root_val(letter)


    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        treeM = self.morse_tree
        for i in code_str:
            if i == '.':
                treeM = treeM.get_child_left()
            else:
                treeM = treeM.get_child_right()
            if not treeM:
                return None
        return treeM.get_root_val()

    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        if tree is None:
            return False        
        elif tree.get_root_val() == letter:
            return path
        else:
            return self.find_path(tree.get_child_left(), letter, path+'.') or self.find_path(tree.get_child_right(), letter, path+'-')
        

    def encode(self, msg: str):
        """Encode a message"""
        code = ''
        path = ''
        for i in msg.split():
            for j in i:
                mes1 = self.find_path(self.morse_tree, j, path)
                if mes1:
                    code += str(mes1) + ' '
                else:
                    raise ValueError ('Could not encode {}: {} is not in the tree'.format(msg, j))    
        return code

    def decode(self, code: str):
        """Decode a message"""
        msg = ''
        for letter in code.split():
            mes = self.follow_and_retrieve(letter)
            if mes:
                msg += mes
            else:
                raise ValueError ('Could not decode {}: {} is not in the tree'.format(code, code)) 
        return msg


def main():
    morse_coder = Coder("data/projects/morse/morse.txt")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print("Encoded : {}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded : {}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded : {}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))


if __name__ == "__main__":
    main()
