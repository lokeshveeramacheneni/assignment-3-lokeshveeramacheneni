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


def iterative_deepening_depth_first_search(maze_map, tree, start_pos, goal_pos):
    """Function to implement the DFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [list]
        [Contians the raw data of the map]
    tree    :   [dictionary]
        [Dictionary containing the parents and childs of the tree]
    start_pos : [tuple]
        [Contains the starting position of the map]
    goal_pos : [tuple]
        [Contains the goal positions of the map]

    Returns
    -------
    [list]
        [Returns the list containing the traversed map]
    """
    #start = start_pos[0]
    #goal = goal_pos
    #queue = deque([("", start)])
    # Fill in your iterative deepening DFS algorithm here
    # Depth limit counter for maintaining the depth
    depth_limit = -1
    maze_map_list = list()
    maze_map_do = []
    # Visited list for storing the data of visited nodes
    visited_pos = []
    flag = 0
    # Converting the list of strings to list of characters  
    for line in maze_map:
        maze_map_list.append(list(line))
    while(1):
        # Increment the depth limit for every iteration
        depth_limit += 1
        # Initializing the stack for depth first search traversal
        stack = []
        stack.append(start_pos)
        visited_pos = []
        position = stack.pop()
        visited_pos.append(position)
        # Initializing the depth counter to calculate the current depth
        depth_counter = -1
        childs = []
        while(1):
            # At initial stage increment the depth counter
            if len(stack) == 0:
                depth_counter += 1
            # Assigning the character to node and printing the list for live updates
            if len(position) > 2 and maze_map_list[position[1]][position[0]] == ' ':
                maze_map_list[position[1]][position[0]] = assign_character_for_nodes(position[2])
                os.system('clear')
                for line in maze_map_list:
                    print("".join(line)[:-1])
            # If current depth is less than depth limit then expand the nodes
            # and add it to stack and visitied node list
            if depth_counter < depth_limit:
                childs = tree[tuple([position[0],position[1]])]
                childs.reverse()
                depth_counter += 1
                for each_child in childs:
                    if tuple([each_child[0],each_child[1]]) not in visited_pos:
                        stack.append(each_child)
                        visited_pos.append(tuple([each_child[0],each_child[1]]))
            # If stack is not empty the update
            # position from stack and if the stack is empty
            # break the loop
            if len(stack) != 0:
                position = stack.pop()
                #print("POS: ",position)
            else:
                break
            # If the current depth is greater than limit then
            # stop the loop 
            if depth_counter > depth_limit:
                break
            # Logic to assign the current node level
            node_level = abs(position[0]-start_pos[0]) + abs(position[1]-start_pos[1])
            depth_counter = node_level
        # Checking whether the map has spaces if no then stop iterations
        # or stop after particular depth
        p = [x for x in  maze_map_list if x.count(' ') != 0 ]
        if len(p) == 0 or depth_limit > 86:
            break
    maze_map_new = []
    # Converting the list of charachters to strings
    for list_1 in maze_map_list:
        new_val = "".join(list_1)
        maze_map_new.append(new_val[:-1])
    # Returning the list of strings to write on file
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
    # Reading the 3 maps and converting to tree
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
    # Iterative deeepening search for map 1
    start_pos_map1 = tree_1['root']
    goal_pos_map1 = tree_1['goal']
    path_map1 = iterative_deepening_depth_first_search(maze_map_map1, tree_1, start_pos_map1, goal_pos_map1)
    write_to_file("iddfs_map1", path_map1)
    # Iterative deepening search for map 2
    start_pos_map2 = tree_2['root']
    goal_pos_map2 = tree_2['goal']
    path_map2 = iterative_deepening_depth_first_search(maze_map_map2, tree_2, start_pos_map2, goal_pos_map2)
    write_to_file("iddfs_map2", path_map2)
    # Iterative deepening search for map 3
    start_pos_map3 = tree_3['root']
    goal_pos_map3 = tree_3['goal']
    path_map3 = iterative_deepening_depth_first_search(maze_map_map3, tree_3, start_pos_map3, goal_pos_map3)
    write_to_file("iddfs_map3", path_map3)