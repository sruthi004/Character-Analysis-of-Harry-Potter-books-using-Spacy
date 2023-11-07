# Imports
import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import networkx as nx
import matplotlib.pyplot as plt
#!python -m spacy download en_core_web_sm
import PyPDF2
import os
from utils import *

# Pipeline for getting graph for each of the 7 books

# Load spacy english language model
NER = spacy.load('en_core_web_sm') #,disable=['parser', 'tagger','ner']
NER.max_length = 1562040

# Load and process web scraped csv file
names = process_csv("Character Analysis of Harry Potter books using Spacy\\characters.csv")

# Load all books from path
all_books = [i for i in os.scandir("Character Analysis of Harry Potter books using Spacy\\books") if '.pdf' in i.name]
books_graph = []
for book in all_books: #
    text = get_text(book)
    book_doc = NER(text)
    entity_df = get_entity(book_doc)

    # Apply filter_entity function and remove empty lists
    entity_df['character_entities'] = entity_df['entities'].apply(lambda x: filter_entity(x, names))
    entity_df_filtered = entity_df[entity_df['character_entities'].map(len)>0]
    entity_df_filtered = entity_df_filtered.reset_index(drop=True)
    relationships_df = iden_relationships(entity_df_filtered,names)
    

    # Create graph for each book and create list
    graph = nx.from_pandas_edgelist(relationships_df,
                               source = 'source',
                               target = 'target',
                               edge_attr = 'value',
                               create_using = nx.Graph())

    books_graph.append(graph)


# Creating a list of degree centrality of all the books
evol = [nx.degree_centrality(book) for book in books_graph]

# Creating a DataFrame from the list of degree centralities in all the books
degree_evol_df = pd.DataFrame.from_records(evol)

# Plotting the degree centrality evolution of 5 main characters
degree_evol_df[["Harry", "Ron", "Hermione", "Dumbledore", "Voldemort"]].plot()
