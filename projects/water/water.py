'''Water jugs project

Author: Beka Beriashvili

'''
#!/usr/bin/env python3
#encoding: UTF-8


JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    '''State of the jugs'''
    def __init__(self, jug_1: int, jug_2: int):
        '''__init__'''
        self._jug_1 = jug_1
        self._jug_2 = jug_2

    def __eq__(self, other: object):
        '''__eq__'''
        return self._jug_1 == other._jug_1 and self._jug_2 == other._jug_2

    def __str__(self):
        '''__str__'''
        return '(' + str(self._jug_1) + ', ' + str(self._jug_2) + ')'



    def clone(self):
        '''Copy a state'''
        return State(self._jug_1, self._jug_2)


    def fill_jug_1(self):
        '''Fill jug1 to capacity from the pump'''
        self._jug_1 = JUG_1_MAX
        return self

    def fill_jug_2(self):
        '''Fill jug2 to capacity from the pump'''
        self._jug_2 = JUG_2_MAX
        return self

    def empty_jug_1(self):
        '''Pour the water from jug1 onto the ground'''
        self._jug_1 = 0
        return self

    def empty_jug_2(self):
        '''Pour the water from jug2 onto the ground'''
        self._jug_2 = 0
        return self

    def pour_jug_1_to_jug_2(self):
        '''Pour as much water as you can from jug1 to jug2 without spilling'''
        while self._jug_1 > 0 and self._jug_2 < 3:
            self._jug_1 -=1
            self._jug_2 +=1
        return self    


    def pour_jug_2_to_jug_1(self):
        '''Pour as much water as you can from jug2 to jug1 without spilling'''
        while self._jug_1 < 5 and self._jug_2 > 0:
            self._jug_1 +=1
            self._jug_2 -=1
        return self    


def search(start_state: object, goal: object, moves_lst: list):
    '''Find a sequence of states'''

    moves_lst.append(start_state)
    list1 = [start_state.clone().fill_jug_1(), start_state.clone().fill_jug_2(), start_state.clone().empty_jug_1(), 
             start_state.clone().empty_jug_2(), start_state.clone().pour_jug_1_to_jug_2(),
             start_state.clone().pour_jug_2_to_jug_1()
            ]

    for i in list1:
        if i ==goal:
            return moves_lst.append(i)

        elif i in moves_lst:
            pass
        else:
            return search(i, goal, moves_lst)   
     
    




def main():
    '''Main function'''
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(', '.join([str(s) for s in moves]))


if __name__ == '__main__':
    main()
