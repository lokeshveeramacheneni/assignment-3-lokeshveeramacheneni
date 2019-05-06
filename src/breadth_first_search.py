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


def breadth_first_search(maze_map, tree, start_pos, goal_pos):
    """Function to implement the BFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [list]
        [Contains the raw map in list of strings]
    tree    :   [dictionary]
        [Contains the tree which has all parents and childs relations]
    start_pos : [tuple]
        [Contains the starting position of the tree]
    goal_pos : [tuple]
        [Contains the goal positions of the tree]

    Returns
    -------
    [list]
        [Returns the traversed map in list of strings]
    """
    # Fill in your BFS algorithm here
    # Initializing the queue
    queue = deque(start_pos)
    y = queue.pop()
    x = queue.pop()
    # List for storing the visited nodes
    visited_pos = []
    visited_pos.append(tuple([x,y]))
    maze_map_list = list()
    #Coverting the list of strings to list of characters to make the changes the map
    for line in maze_map:
        maze_map_list.append(list(line))
    while(1):
        # Getting the childs for the node
        childs = list(tree[(x,y)])
        for each_child in childs:
            # If the child is not visited add it to queue and add to visitied
            if tuple([each_child[0],each_child[1]]) not in visited_pos:
                if maze_map_list[each_child[1]][each_child[0]] == ' ':
                    assigned_character = assign_character_for_nodes(each_child[2])
                    maze_map_list[each_child[1]][each_child[0]] = assigned_character
                    # Print the map on the terminal for live updates
                    os.system('clear')
                    for line in maze_map_list:
                        print("".join(line)[:-1])  
                queue.append(tuple([each_child[0],each_child[1]]))
                visited_pos.append(tuple([each_child[0],each_child[1]]))
        # Get the next element from queue
        pop_elemnt = queue.popleft()
        # If the queue is empty exit the loop
        if pop_elemnt == 'root'or len(queue) == 0:
            break
        x = pop_elemnt[0]
        y = pop_elemnt[1]
    maze_map_new = []
    # Converting the list of charachters to list of strings for 
    # writing onto a file 
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
    # Reading the three maps and converting to trees 
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
    # Calling the breadthe first search on first map
    start_pos_map1 = tree_1['root']
    goal_pos_map1 = tree_1['goal']
    path_map1 = breadth_first_search(maze_map_map1, tree_1, start_pos_map1, goal_pos_map1)
    write_to_file("bfs_map1", path_map1)
    # Breadth first search on second map
    start_pos_map2 = tree_2['root']
    goal_pos_map2 = tree_2['goal']
    path_map2 = breadth_first_search(maze_map_map2, tree_2, start_pos_map2, goal_pos_map2)
    write_to_file("bfs_map2", path_map2)
    # Breadth first search on thrid map
    start_pos_map3 = tree_3['root']
    goal_pos_map3 = tree_3['goal']
    path_map3 = breadth_first_search(maze_map_map3, tree_3, start_pos_map3, goal_pos_map3)
    write_to_file("bfs_map3", path_map3)
