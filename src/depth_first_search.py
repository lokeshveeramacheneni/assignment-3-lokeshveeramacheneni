#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import sys
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes


def depth_first_search(maze_map, tree, start_pos, goal_pos):
    """Function to implement the DFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [list]
        [Contains the raw map data to be traversed]
    tree    :   [dictionary]
        [Contains the tree to traverse]
    start_pos : [tuple]
        [Contains the data of start position in a tuple]
    goal_pos : [tuple]
        [Contains the data for goal positions in a tuple]

    Returns
    -------
    [list]
        [Returns the list containing the traversed map]
    """
    #start = start_pos[0]
    #goal = goal_pos
    #queue = deque([("", start)])
    # Fill in your DFS algorithm here
    # Initializing the stack 
    stack = []
    stack.append(start_pos)
    # List to store the visitied nodes
    visited_pos = []
    position = stack.pop()
    visited_pos.append(position)
    maze_map_list = list()
    maze_map_do = []
    # Converting the list of strings to list of characters (Strings are immutable)
    for line in maze_map:
        maze_map_list.append(list(line))
    while(1):
        # Assigning the charachter to the particular node
        if len(position) > 2 and maze_map_list[position[1]][position[0]] == ' ':
            maze_map_list[position[1]][position[0]] = assign_character_for_nodes(position[2])
        # Getting the childs for the particular node
        childs =  tree[tuple([position[0],position[1]])]
        childs.reverse()
        for each_child in childs:
            # For every child if it is not visited add to stack and to visited list
            if tuple([each_child[0],each_child[1]]) not in visited_pos:
                stack.append(each_child)
                visited_pos.append(tuple([each_child[0],each_child[1]]))
            # Printing the list for live updates on console
            os.system('clear')
            for line in maze_map_list:
                print("".join(line)[:-1])
        # If stack is empty then break
        if  len(stack) == 0:
            break
        pop_element = stack.pop()
        # Update the last element of stack as new node
        position = pop_element
    maze_map_new = []
    # Returning the list of strings from list of characters 
    # to write on to a file
    for list_1 in maze_map_list:
        new_val = "".join(list_1)
        maze_map_new.append(new_val[:-1])
    return maze_map_new


if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')
    # Reading the 3 maps and converting them to trees
    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()
    tree_1 = maze_map_to_tree(maze_map_map1)
    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()
    tree_2 = maze_map_to_tree(maze_map_map2)
    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()
    tree_3 = maze_map_to_tree(maze_map_map3)
    # CALL THIS FUNCTIONS after filling in the necessary implementations
    # Depth first search traversal for map 1
    start_pos_map1 = tree_1['root']
    goal_pos_map1 = tree_1['goal']
    path_map1 = depth_first_search(maze_map_map1, tree_1, start_pos_map1, goal_pos_map1)
    write_to_file("dfs_map1", path_map1)
    # Depth first search traversal for map 2
    start_pos_map2 = tree_2['root']
    goal_pos_map2 = tree_2['goal']
    path_map2 = depth_first_search(maze_map_map2, tree_2, start_pos_map2, goal_pos_map2)
    write_to_file("dfs_map2", path_map2)
    # Depth first search traversal for map 3
    start_pos_map3 = tree_3['root']
    goal_pos_map3 = tree_3['goal']
    path_map3 = depth_first_search(maze_map_map3, tree_3, start_pos_map3, goal_pos_map3)
    write_to_file("dfs_map3", path_map3)
