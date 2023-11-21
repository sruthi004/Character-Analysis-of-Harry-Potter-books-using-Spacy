#### Character Analysis of Harry Potter books using Spacy

**Aim:**
* Main goal of this project is to identify the main characters in the books and analyse the strength of relationship that exists between them.
* Libraries used would include Spacy, NetworkX, Pyvis, Pandas, Numpy, Matplotlib.

 **Steps:**
 * Character names from all the 7 Harry potter books was obtained through a small web scraping project and preprocessing was done.
 * NER was extracted from all books and filtered out so that we have only names from the web scraped file.
 * Names from each 10 sentences were taken (window_size = 10) and grouped together to get a dataframe which shows the strength of relationship between two characters.
 * Graphs were created to visualize the extracted relationships.

**Inferences:**
* Strongest relationship was seen for the below characters.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/0871cd9d-7198-49dc-8929-863dc3c953c9)

* Throughout the books, Voldemort seems to have the strongest relationship with the below characters.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/8a26980a-ae8b-46ec-8b36-7eaba276a4a7)

* Overall, the importance of top characters varies as shown in the below graph.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/af7ed68c-b5d2-4996-b425-1fdf741601f7)

* **Centrality measures** are a vital tool for understanding networks, often also known as graphs. These algorithms use graph theory to calculate the importance of any given node in a network.
* Three centrality measures were calculated : Degree_centrality, Betweenness_centrality, Closeness_centrality.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/50eb36a5-7893-4c0b-8185-9cf627c19c65)

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/899686cc-3684-4cba-9b09-7ff35351010c)

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/8ceb9ffb-0394-497e-b0bd-ff3d5c10c00a)

* Finally, graphs were plotted with the characters extracted from all 7 books using NetworkX and Pyvis.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/9ad3ee26-2330-4d83-b688-42eb9cfafc5c)

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/36fd8ffc-30a4-4907-94c4-317cca852a3a)




