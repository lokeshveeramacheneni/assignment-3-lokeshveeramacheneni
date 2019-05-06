#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

import sys
import os
import time


def maze_map_to_tree(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : [list]
        [Containing the raw data of the map]

    Returns
    -------
    [dictionary]
        [Contains the data of parent and child for all nodes in tree]
    """
    interim_input = []
    pos_x = 0
    pos_y = 0
    goal_pos = list()
    # Converting the list of strings to charachters and 
    # storing the values of start and goal positions
    for line in maze_map:
        if 's' in line:
            pos_x = line.index('s')
            pos_y = maze_map.index(line)
        if '*' in line:
            pos = (line.index('*'),maze_map.index(line))
            goal_pos.append(pos)
        interim_input.append(list(line))
    # Initializing the dictionary to store nodes
    tree_dict = dict()
    input_list = []
    # Logic to store the nodes of child for a particular parent
    # Child nodes are stored in 
    # (x_position, y_position, direction_to_parent) format
    for y in range(1,len(interim_input)-1):
        for x in range(1,len(interim_input[0])-2):
            input_list = [(x,y-1,'N'),(x+1,y,'E'),(x,y+1,'S'),(x-1,y,'W')]
            if interim_input[y-1][x] == '=' or interim_input[y-1][x] == '|':
                input_list.remove(tuple([x,y-1,'N']))
            if interim_input[y][x+1] == '=' or interim_input[y][x+1] == '|':
                input_list.remove(tuple([x+1,y,'E']))
            if interim_input[y+1][x] == '=' or interim_input[y+1][x] == '|':
                input_list.remove(tuple([x,y+1,'S']))
            if interim_input[y][x-1] == '=' or interim_input[y][x-1] == '|':
                input_list.remove(tuple([x-1,y,'W']))
            if len(input_list) != 0:
                tree_dict[(x,y)] = input_list
    # Storing the start position and goal position
    # in the tree with key as 'root' and 'goal'.
    tree_dict['root'] = (pos_x,pos_y)
    tree_dict['goal'] = tuple(goal_pos)
    return tree_dict  
    

    #raise NotImplementedError


def assign_character_for_nodes(maze_map_charac):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    maze_map_charac : [character]
        [Contains the direction of child with respect to the parent]

    Returns
    -------
    [character]
        [The specific character the input]
    """
    # Based on the direction_to_parent in child node
    # corresponding character is assigned
    character_to_assign = ' '
    if maze_map_charac == 'N':
        character_to_assign = "\u2534"
    elif maze_map_charac == 'E':
        character_to_assign = "\u251c"
    elif maze_map_charac == 'S':
        character_to_assign = "\u252c"
    elif maze_map_charac == 'W':
        character_to_assign = "\u2524"
    return character_to_assign
    #raise NotImplementedError


def write_to_file(file_name, path):
    """Function to write output to console and a txt file.
    Please ensure that it should ALSO be possible to visualize each and every
    step of the tree traversal algorithm in the map in the console.
    This enables understanding towards the working of your
    tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    filen_name : string
        This parameter defines the name of the txt file.
    path : [type]
        [description]

    """
    # Writing the tarversed tree data to text file
    with open(file_name,'w') as f:
        for each_line in path:
            f.write("%s\n"%each_line)
    # raise NotImplementedError
