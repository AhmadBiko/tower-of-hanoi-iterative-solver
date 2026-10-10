def hanoi_solver(number):
    total_moves = 2 ** number - 1

    left = []
    middle = []
    right = []
    path = ''

    #[1] inserting the disks to start the game
    for disk in range(number):
        left.append(number - disk)
        
    path += str(left) + ' ' + str(middle) + ' ' + str(right) + '\n'

    #[2] solving the puzzle step by step
    for i in range(1, total_moves + 1):

        #[3] ODD MOVES: moving disk 1
        if i % 2 != 0:

            if number % 2 != 0:  # for odd cases (1, 3, 5)

                #[4] left -> right -> middle -> left
                if 1 in left:
                    right.append(left.pop())
                elif 1 in right:
                    middle.append(right.pop())
                elif 1 in middle:
                    left.append(middle.pop())

            else:  # for even cases (2, 4, 6)

                #[5] left -> middle -> right -> left
                if 1 in left:
                    middle.append(left.pop())
                elif 1 in middle:
                    right.append(middle.pop())
                elif 1 in right:
                    left.append(right.pop())

        #[6] EVEN MOVES: moving the smaller disk between the two rods NOT containing 1
        else:
            #[7] finding the two rods without disk 1
            rods = [r for r in [left, middle, right] if 1 not in r]
            rod_A, rod_B = rods[0], rods[1]

            if not rod_A:
                rod_A.append(rod_B.pop())
            elif not rod_B:
                rod_B.append(rod_A.pop())
            elif rod_A[-1] < rod_B[-1]:
                rod_B.append(rod_A.pop())
            else:
                rod_A.append(rod_B.pop())

        #[8] appending the current state to path
        path += str(left) + ' ' + str(middle) + ' ' + str(right) + '\n'
    return path.strip()

#[9]testing data
print(hanoi_solver(1))
print(hanoi_solver(2))
print(hanoi_solver(3))
print(hanoi_solver(4))
print(hanoi_solver(5))