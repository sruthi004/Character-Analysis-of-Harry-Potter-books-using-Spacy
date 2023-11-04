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
from src.utils import *

# Pipeline for getting graph for each of the 7 books

# Load spacy english language model
NER = spacy.load('en_core_web_sm')
# Load all books from path
all_books = [i for i in os.scandir("C:\\Users\\sruth\\Desktop\\Work\\Git_projects\\Character Analysis of Harry Potter books using Spacy\\books") if '.pdf' in i.name]

for book in all_books:
    book_doc = get_text(book)


