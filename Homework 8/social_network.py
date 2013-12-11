# Name: ...
# Evergreen Login: ...
# Computer Science Foundations
# Programming as a Way of Life
# Homework 8

import networkx as nx
import matplotlib.pyplot as plt
import operator
import random


###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_node("A")
practice_graph.add_node("B")
practice_graph.add_node("C")
practice_graph.add_node("D")
practice_graph.add_node("E")
practice_graph.add_node("F")

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("D", "C")
practice_graph.add_edge("F", "C")
practice_graph.add_edge("F", "D")
practice_graph.add_edge("D", "E")

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

def draw_practice_graph():
    """Draw practice_graph to the screen."""
    nx.draw(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph()


###
### Problem 1b
###

rj = nx.Graph()

people = ['Nurse', 'Juliet', 'Tybalt', 'Capulet', 'Romeo', 'Benvolio', 'Montague', 'Friar Laurence', 'Escalus', 'Mercutio', 'Paris']

for p in people:
    rj.add_node(p)
  
relations = [(0, 1), (1, 2), (1, 3), (2, 3), (1, 7), (1, 4), (3, 8), (3, 10), (4, 7), (4, 5), (4, 6), (4, 9), (5, 6), (6, 8), (8, 9), (8, 10), (9, 10)]

for i in relations:
    first = i[0]
    second = i[1]
    rj.add_edge(people[first], people[second])

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

def draw_rj():
    """Draw the rj graph to the screen and to a file."""
    nx.draw(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
draw_rj()


###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    The parameter 'user' is the string name of a person in the graph.
    """
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given graph.
    The result does not include the given user nor any of that user's friends.
    """
    setfriendoffriend = set()
    setfriends = friends(graph, user)
    for f in setfriends:
        temp = friends(graph, f)
        setfriendoffriend.update(temp)
    setfriendoffriend.remove(user)
    for f in setfriends:
        if (f in setfriendoffriend):
            setfriendoffriend.remove(f)
    return setfriendoffriend


assert friends_of_friends(rj, "Mercutio") == set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common."""
    friends1 = friends(graph, user1)
    friends2 = friends(graph, user2)
    commonfriends = friends1.intersection(friends2)
    return commonfriends

assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])

assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map from each user U to the number of friends U has in common with the given user.
    The map keys are the users who have at least one friend in common with the
    given user, and are neither the given user nor one of the given user's friends.
    Take a graph G for example:
        - A and B have two friends in common
        - A and C have one friend in common
        - A and D have one friend in common
        - A and E have no friends in common
        - A is friends with D
    number_of_common_friends_map(G, "A")  =>   { 'B':2, 'C':1 }
    """
    commonnumbers = dict()
    fof = friends_of_friends(graph, user)
    for f in fof:
        temp = common_friends(graph, user, f)
        commonnumbers[f] = len(temp)
    return commonnumbers

assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}

assert number_of_common_friends_map(rj, "Mercutio") == { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map):
    """Given a map whose values are numbers, return a list of the keys.
    The keys are sorted by the number they map to, from greatest to least.
    When two keys map to the same number, the keys are sorted by their
    natural sort order, from least to greatest."""
    mapkeys = map.keys()
    listkeys = list(mapkeys)
    listsorted = list()
    for k in mapkeys:
        currentkey = None
        max = 0
        for i in listkeys:
            if (map[i] > max or (map[i] == max and currentkey > i)):
                currentkey = i
                max = map[i]
        listsorted.append(currentkey)
        listkeys.remove(currentkey)
    return listsorted
    
    
assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the number of common friends.
    """
    map = number_of_common_friends_map(graph, user)
    friendrec = number_map_to_sorted_list(map)
    return friendrec


assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']

assert recommend_by_number_of_common_friends(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map from each user U to the friend influence, with respect to the given user.
    The map only contains users who have at least one friend in common with U,
    and are neither U nor one of U's friends.
    See the assignment for the definition of friend influence.
    """
    print "To be implemented"

assert influence_map(rj, "Mercutio") == { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names of people in the graph
    who are not yet a friend of the given user.
    The order of the list is determined by the influence measurement.
    """
    print "To be implemented"

assert recommend_by_influence(rj, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###



###
### Problem 5
###

# (There is no code to write for this problem.)


###
### Problem 6
###

# (There is no code to write for this problem.)


###
### Problem 7
###


###
### Problem 8
###

# (Your code goes here.)

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090


###
### Problem 9
###


###
### Problem 10
###


###
### Problem 11
###


###
### Problem 12
###
