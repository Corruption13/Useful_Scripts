#Name: S Sandeep Pillai
#College: Model Engineering College (CS-1 A)
#Number: 9562294830
#PYTHON 3
### Program to do Matrix Algebera - Add - Subtract - Multiply

class matrix:       # Class used for storing, inputing and outputing matrices.

    def __init__(self, row=-1,column=-1):  # Initialise values as -1 for empty matrix.
        self.column = column
        self.row = row
        self.M = [["0" for i in range(self.column)] for j in range(self.row)] # Empty Matrix consisting of 0's


    def input(self):
        self.row = int(input("Enter number of rows: "))
        self.column  = int(input("Enter number of collumns: "))
        print("Enter the values of matrix elements:" , self.row , '*' , self.column)
        self.M = [[int(input(" = ")) for i in range(self.column)] for j in range(self.row)]  # Inputs the Matrix


    def output(self):
        if self.row == -1:
            print("Empty")
        for i in range(self.row):
            for j in range(self.column):
                print(self.M[i][j], end=' ')
            print("")

    def getitem(self, i, j):        # Can't access private variables of class directly.
            return self.M[i][j]
    def putitem(self, i, j, val):
            self.M[i][j] = val
#END OF CLASS MATRIX

class matrix_algebra:       # Class encapsulates all algebraic functions.

    def add(X = matrix(), Y= matrix()):

        if X.row == Y.row !=-1 and X.column == Y.column !=-1:
            S = matrix(X.row, Y.column)  # Python uses call by Reference.. Hence need to create dummy variable.
            for i in range(X.row):
                for j in range(Y.column):
                    value = X.getitem(i,j) + Y.getitem(i,j)
                    S.putitem(i, j, value)


            S.output()
            del S       ### VERY IMPORTANT TO RESET VALUE OF DUMMY VARIABLE!!
        else:
            print("Matrix dimensions incompatible for addition")

    def sub(X = matrix(), Y= matrix()):

        if X.row == Y.row !=-1 and X.column == Y.column !=-1:
            S = matrix(X.row, X.column) # Dummy matrix of same dimensions
            for i in range(X.row):
                for j in range(X.column):
                    value = X.getitem(i,j) - Y.getitem(i,j)
                    S.putitem(i, j, value)

            S.output()
            del S
        else:
            print("Matrix dimensions incompatible for subtraction")

    def mult(X = matrix, Y = matrix):

        if X.column == Y.row:
            S = matrix(X.row, Y.column)
            for i in range(X.row):
                for j in range(Y.column):
                    sum = 0
                    for k in range(Y.row):
                        sum = sum + X.getitem(i, k) * Y.getitem(k, j)

                    S.putitem(i, j, sum)
            S.output()
            del S
        else:
            print("Matrix dimensions incompatible for multiplication")
# END OF ALL FUNCTIONS AND CLASSES

# START OF PROGRAM CONTROL
A = matrix()
B = matrix()

def mainmenu():
    exit = False
    while(exit == False):
        print("Matrix A: ")
        A.output()
        print("Matrix B: ")
        B.output()
        print("[A] Enter value of matrix 'A'", "\n[B] Enter value of matrix 'B'", "\n\n[1] Add A and B")
        print("[2] Subtract A and B","\n[3] Multiply A and B", "\n\n[0] Exit Program")
        ch = input("Enter a choice:")
        if ch == '0':
            exit = True
        elif ch == 'a' or ch =='A':
            print("Enter attributes for Matrix A ")
            A.input()
        elif ch == 'b' or ch =='B':
            print("Enter attributes for Matrix B ")
            B.input()
        elif ch == '1' or ch == '+':
            matrix_algebra.add(A, B)
        elif ch == '2' or ch == '-':
            matrix_algebra.sub(A, B)
        elif ch == '3' or ch == '*':
            matrix_algebra.mult(A, B)
        input("\nPress any Button")
        print('\n'*42) # Hehe, solves the cross platform clear screen problem.

mainmenu()