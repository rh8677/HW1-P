# This is the file for the word search algorithm.
#
# Author: Raymond Hu rh8677
from collections import deque
import sys


# Find all the similar words to 'word' in the dictionary
def find_neighbors(word, dictionary):
    neighbors = set()

    # If there is a 1 letter difference, it is considered
    # a 'neighbor'
    for test in dictionary:
        count = 0
        for i in range(len(word)):
            if test[i] != word[i]:
                count += 1
        if count == 1:
            neighbors.add(test)

    return neighbors


# The search function
def word_search(one, two, dictionaries):
    visited = {one}
    queue = deque([(one, [])])

    # Performs bfs to find the path from the
    # starting word to the goal
    while queue:
        current, path = queue.popleft()
        visited.add(current)
        for neighbor in dictionaries[current]:
            if neighbor == two:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)

    return None


# Runs the three test cases
def print_cases(word_list):

    # Test case 1 - "cold" to "warm"
    graph = {}
    for j in word_list:
        if len(j) == len("cold"):
            graph[j] = 1
    for i in graph:
        graph[i] = find_neighbors(i, graph)
    # Prints solution (if found)
    solution = word_search("cold", "warm", graph)
    print()
    print("The path from cold to warm is:")
    for i in solution:
        print(i + " ")

    # Test case 2 - "small" to "short"
    graph = {}
    for j in word_list:
        if len(j) == len("small"):
            graph[j] = 1
    for i in graph:
        graph[i] = find_neighbors(i, graph)
    # Prints solution (if found)
    solution = word_search("small", "short", graph)
    print()
    print("The path from small to short is:")
    for i in solution:
        print(i + " ")

    # Test case 3 - "ten" to "two"
    graph = {}
    for j in word_list:
        if len(j) == len("adobe"):
            graph[j] = 1
    for i in graph:
        graph[i] = find_neighbors(i, graph)
    # Prints solution (if found)
    solution = word_search("adobe", "party", graph)
    print()
    print("The path from adobe to party is:")
    for i in solution:
        print(i + " ")


# The initialization and calling of the search function
if __name__ == '__main__':

    # Puts all the words of the dictionary into the array
    diction = {}
    with open("dict.txt") as file:
        while line := file.readline().rstrip():
            diction[line] = 1

    # Shows the result of 3 test cases (1 custom)
    print_cases(diction)

    # User input requests and validation
    print()
    print("Welcome to Word Search!")
    first = input("What word do you want to start from?\n")
    if first not in diction:
        print("This word does not exist in the dictionary.")
        sys.exit()
    second = input("What word do you want to end with?\n")
    if len(first) != len(second):
        print("The word lengths do not match.")
        sys.exit()
    if first == second:
        print("The words are the same.")
        sys.exit()
    if second not in diction:
        print("This word does not exist in the dictionary.")
        sys.exit()

    # Put all the words of the same length as the input words
    # into a separate graph
    graph = {}
    for j in diction:
        if len(j) == len(first):
            graph[j] = 1
    for i in graph:
        graph[i] = find_neighbors(i, graph)

    # Prints solution (if found)
    solution = word_search(first, second, graph)
    if solution:
        print("The path from " + first + " to " + second + " is:")
        for i in solution:
            print(i + " ")
    else:
        print("There is no connection between the two words.")

