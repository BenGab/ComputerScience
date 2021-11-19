from csp import Constraint, CSP
from typing import List, Dict, Optional

class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters
    
    def satisfied(self, assigment: Dict[str, int]) -> bool:
        if len(set(assigment.values())) < len(assigment):
            return False

        if len(assigment) == len(self.letters):
            s: int = assigment["S"]
            e: int = assigment["E"]
            n: int = assigment["N"]
            d: int = assigment["D"]
            m: int = assigment["M"]
            o: int = assigment["O"]
            r: int = assigment["R"]
            y: int = assigment["Y"]
            send: int = s * 1000 + e * 100 + n * 10 + d
            more: int = m * 1000 + o * 100 + r * 10 + e
            money: int = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True

if __name__ == "__main__":
    letters: List[str] = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    possible_digits: Dict[str, List[int]] = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_digits["M"] = [1]
    csp: CSP[str, int] = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution: Optional[Dict[str, int]] = csp.bracktracking_search()
    if solution is None:
        print("no solution found")
    else:
        print(solution)