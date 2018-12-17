'''Build a ladder of words using stacks and queues


Author: Beka Beriashvili
'''
#!/usr/bin/env python3

WORDS_OF_3 = set()
WORDS_OF_4 = set()
WORDS_OF_5 = set()


class Stack:
    '''Implementing Stack ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''Is stack empty?'''
        return self.items == []
    def size(self):
        '''Return stack size'''
        return len(self.items)
    def push(self, item):
        '''Add new item to stack'''
        self.items.append(item)
    def pop(self):
        '''Remove an item from stack'''
        return self.items.pop()
    def peek(self):
        '''Look at the top item'''
        return self.items[-1]
    def clone(self):
        '''Cloning a stack'''
        CloneStack = Stack()
        CloneStack.items = self.items[:]
        return CloneStack


class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []
    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)
    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()
    def size(self):
        '''How big is it?'''
        return len(self.items)


def read_file(filename: str) -> dict:
    '''Read a file into 3 sets'''
    infile = open(filename, 'r')
    for i in infile:
        words = i.rstrip()
        if len(words) == 3:
            WORDS_OF_3.add(words)
        elif len(words) == 4:
            WORDS_OF_4.add(words)
        elif len(words) == 5:
            WORDS_OF_5.add(words)
    return {3: len(WORDS_OF_3), 4: len(WORDS_OF_4), 5: len(WORDS_OF_5)}        


def distance(word1: str, word2: str) -> int:
    '''Differences between words'''
    WordDist = 0
    for a, b in zip(word1, word2):
        if a != b:
            WordDist = WordDist + 1
    return WordDist        


def diff_by_one_all(word, all_words, words1):
    '''Find all words that differ by 1 letter'''
    words = []
    for i in all_words:
        if distance(word, i)==1 and i not in words1:
            words.append(i)
    return words

def main():
    '''Main function'''
    read_file('data/projects/words/words.txt')

    word_start = 'stone'
    word_stop = 'water'
    found = False
    if len(word_start) != len(word_stop):
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    if (len(word_start)) == 3:
        words_to_use = WORDS_OF_3
    elif (len(word_start)) == 4:
        words_to_use = WORDS_OF_4
    elif (len(word_start)) == 5:
        words_to_use = WORDS_OF_5
    else:
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    
    print("Let's turn '%s' into '%s'" % (word_start, word_stop))
    
    NewStack = Stack()
    NewStack.push(word_start)
    NewQueue = Queue()
    NewQueue.enqueue(NewStack)
    words1 = set()
    words1.add(word_start)

    while not found and not NewQueue.is_empty(): 
        deqS = NewQueue.dequeue()
        if deqS.peek() == word_stop:
            found = True
        else:
            ListQD = diff_by_one_all(deqS.peek(), words_to_use, words1)
            for i in ListQD:
                Clone_S = deqS.clone()
                words1.add(i)
                Clone_S.push(i)
                NewQueue.enqueue(Clone_S)

   
    if found:
        print('Ladder found!')
        Ladders = []
        for i in range(0, deqS.size()):
            Ladders.append(deqS.pop())
        for j in Ladders:
            print(j)
        
       
    else:
        print('Ladder not found')


if __name__ == '__main__':
    main()
