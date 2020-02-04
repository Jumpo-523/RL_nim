# coding: utf-8


class InvalidNumberError(Exception):
    pass


def c_input():
    inp = input("which_side?\n")
    if inp not in ["right", "left"]:
        print("You have to choose one from ['right', 'left']")
        c_input()
    return inp

class Nim():

    def __init__(self, n_stones=[5,5]):
        self.state = {"right":n_stones[1], "left":n_stones[0]}
        self._turn = 1 #"first player:1, the second player:-1" 
    
    def play(self):
        # import pdb; pdb.set_trace()
        while self.state != {"right":0, "left":0}:
            which_side_to_take = c_input()
            take_n = int(input("How many take ?\n"))
            # forbid the situation where the stone is of minus numbers.
            if self.state[which_side_to_take] - take_n < 0:
                raise InvalidNumberError("You could not take the number of stones")
            self.state[which_side_to_take] -= take_n
            # turn to the opponent player
            self._turn *= -1
            # display
            print(self.state)



class State():
    def __init__(self, l, r):
        self.right = r
        self.left = l
    
    def __repr__(self):
        return f"<State: [{self.left}, {self.right}]>"
    
    def clone(self):
        return State(self.left, self.right)
    
    def __hash__(self):
        raise NotImplementedError

    def __eq__(self):
        raise NotImplementedError


if __name__ == "__main__":
    nim = Nim()
    nim.play()
    
            