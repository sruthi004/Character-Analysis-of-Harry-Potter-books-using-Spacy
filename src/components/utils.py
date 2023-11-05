# Imports
import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import networkx as nx
import matplotlib.pyplot as plt
import PyPDF2
import os
import time

# Function to pre-process web scraped csv file
def process_csv(path):
    # Load web scraped characters data
    names = pd.read_csv(path)
    # Filtering names with more than 3 words
    names['word_count'] = names['character'].apply(lambda x: len(x.split()))
    names = names[(names.word_count==1) | (names.word_count==2)]
    names.drop('word_count',inplace=True, axis=1)

    # First and Last name columns from names
    names['first_name'] = names['character'].apply(lambda x: x.split(' ')[0])
    names['last_name'] = names['character'].apply(lambda x: x.split(' ')[0] if len(x.split(' '))==1 else x.split(' ')[1])
    return names

# Function for getting text from book
def get_text(book):
    # Opening file and Creating a pdf reader object
    file = open(book, 'rb')
    fileReader = PyPDF2.PdfReader(file)

    # Extract text from the book
    page = fileReader.pages[0]
    text = page.extract_text()
    for i in range(1,len(fileReader.pages)):
        page_s = fileReader.pages[i]
        text_s = page_s.extract_text()
        text +=text_s
    return text

# Function to get named entity for each sentence in the book.
def get_entity(book):
    entity = []
    # Create dataframe with sentences and entity in it.
    for i in book.sents:
        entity_list = [ent.text for ent in i.ents]
        entity.append({"sentence":i, "entities":entity_list})
        
    entity_df = pd.DataFrame(entity)
    return entity_df

# Filter out non-entities
def filter_entity(ent_list, df):
    return [ent for ent in ent_list
           if ent in list(df.character)
           or ent in list(df.first_name)
           or ent in list(df.last_name)]

# Function to identify relationships between characters
def iden_relationships(entity_df_filtered,names):
    window_size = 10 # 10 sentences
    relationships = []

    for i in range(entity_df_filtered.index[-1]):
        end_i = min(i+10,entity_df_filtered.index[-1])
        char_list = sum((entity_df_filtered.loc[i:end_i].character_entities), [])
        
        # Removing duplicates from the list
        char_list_unique = np.unique(char_list)
        char_list_unique = list(char_list_unique)
        
        if len(char_list_unique)>1:
            for index, name in enumerate(char_list_unique[:-1]):
                nex = char_list_unique[index+1]
                text = char_list_unique[index] +' '+ nex
                text_c = nex+' '+char_list_unique[index]
                # Removing relationships where same name appears (first and last)
                if (names['character'].isin([text])).sum()==0 and (names['character'].isin([text_c])).sum()==0: 
                    relationships.append({"source":name, "target":nex})
            
    # Creating DataFrame and calculate weightage for each relationship
    relationships_df = pd.DataFrame(relationships)
    
    # Sort values in relationships_df
    relationships_df = pd.DataFrame(np.sort(relationships_df.values, axis = 1), columns = relationships_df.columns)

    # Calculate weightage for each relationship
    relationships_df['value'] = 1
    relationships_df = relationships_df.groupby(['source', 'target'], sort=False, as_index=False).sum()

    return relationships_df