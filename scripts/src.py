#!/usr/bin/python

##Author: Nayanika Bhalla
##Description: This file defines all the functions to be used to execute the project.
##Usage: source src.py

#####################################################

###import all packages required in this script

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import sys


###Function to filter out the interacting proteins with a combined score of < 500.

def filter_score_df(input_data_frame):
    is_greater_than = input_data_frame["combined_score"]>=500
    input_data_frame_filtered = input_data_frame[is_greater_than]
    return input_data_frame_filtered #A subset of the original dataframe that contains the interacting protein sequences with a combined score >500.

###Function to rename the protein names in the columns to valid EnsemblID format

def rename_proteins(input_data_frame):
    input_data_frame_replaced=input_data_frame.replace('9606.', '', regex=True)
    return input_data_frame_replaced

###Function to initialize the network as an object of the Graph in networkx.

def add_edges(input_data_frame):
    input_network = nx.from_pandas_edgelist(input_data_frame, source = "protein1", target = "protein2")
    return input_network


###Function to return a dataframe of protein domains with a node degree >100
def create_degree_greater_dataframe(network_degree, protein_df):
    degree_list_greater=[]
    for node,degree in network_degree.degree:
        if degree>100:
            degree_list_greater.append(node)
    degree_list_greater_dataframe=pd.DataFrame(degree_list_greater, columns=['ENSEMBL_id'])
    combined_greater_df = protein_df[protein_df['Protein stable ID'].isin(degree_list_greater_dataframe['ENSEMBL_id'])]
    return combined_greater_df

###Function to return list of proteins with a node degree <=100
def create_degree_lesser_dataframe(network_degree, protein_df):
    degree_list_lesser=[]
    for node,degree in network_degree.degree:
        if degree<=100:
            degree_list_lesser.append(node)
    degree_list_lesser_dataframe=pd.DataFrame(degree_list_lesser, columns=['ENSEMBL_id'])
    combined_lesser_df = protein_df[protein_df['Protein stable ID'].isin(degree_list_lesser_dataframe['ENSEMBL_id'])]
    return combined_lesser_df

###Function to create and save a boxplot comparing the number of domains of proteins with node degrees >100 to the ones with node degrees <=100.

def create_boxplot(combined_greater, combined_lesser):
    degree_node = {'node degrees >100':[len(combined_greater)], 'node degrees <=100':[len(combined_lesser)]}
    degree_node_df=pd.DataFrame(degree_node)
    boxplot=degree_node_df.boxplot(column=['node degrees >100','node degrees <=100'])
    #plt.savefig("./project/protein_domains_vs_string_degree.png")
    return boxplot
