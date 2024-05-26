"""
Problem 1:
We need to write a program to find the position of a given number in a list
numbers arranged in decreasing order. We also to minimize the number of time
we access elements from list

Input 
1. cards: A list of numbers sorted in decreasing order Eg, [13,11,10,7,4,3,1]
2. query: A number, Whose position in the array is to be determined eg:c 7

Output 
3. position: The position of query in the list cards. Eg 3 in the abovecase(counting from 0)
"""
 
def locate_card(cards, query):
    # Create a variable position with value 0
    position = 0

    # Set up a loop repetion
    while True:
        # Check if element at the current position match the query
        if cards[position] == query:
            return position
        
        # Increament the position
        position +=1
        # check if we have reached the end of the array
        if position == len(cards):
            # Number not found
            return -1

cards = [13,11,10,7,4,3,1]
query = 7
output = 3

test = {
    'input' : {
        'cards': [13,11,10,7,4,3,1],
        'query' : 7
    },
    'output' : 3
}
# query occurs in the middle
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3,1,0],
        'query': 7
    },
    'output': 3
}

tests = []
tests.append(test)

tests.append({
'input': {
'cards': [13, 11, 10, 7, 4, 3, 1, 0],
'query': 1
},
'output': 6
})

# query is the first element
tests.append({
'input': {
'cards': [4, 2, 1, -1],
'query': 4
},
'output': 0
})

# query is the last element
tests.append({
'input': {
'cards': [3, -1, -9, -127],
'query': -127
},
'output': 3
})

#cards contains just one element, query
tests.append({
'input': {
'cards': [6],
'query': 6
},
'output': 0
}) 

# cards does not contain query
tests.append({
'input': {
'cards': [9, 7, 5, 2, -9],
'query': 4
},
'output': -1
}) 

# cards is empty
tests.append({
'input': {
'cards': [],
'query': 7
},
'output': -1
})

# numbers can repeat in cards
tests.append({
'input': {
'cards': [7, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
'query': 3
},
'output ' : 7
}) 

# query occurs multiple times
tests.append({
'input': {
'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
'query': 6
},
'output': 2
})

if __name__ == "__main__":
    result = locate_card(**test['input'])
    final_answer = result == test['output']
    if final_answer:
        print("test case passed")
    else:
        print("test case is failed")


