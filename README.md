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

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/da818355-ba64-4a36-a53b-9413ae736584)

* Overall, the importance of top characters varies as shown in the below graph.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/2ff60a95-8877-420f-b4b0-5751d2aae7f4)

* **Centrality measures** are a vital tool for understanding networks, often also known as graphs. These algorithms use graph theory to calculate the importance of any given node in a network.
* Three centrality measures were calculated : Degree_centrality, Betweenness_centrality, Closeness_centrality.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/46201aef-44ef-4631-b1a1-c576c0e10183)

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/07b66b73-7c8b-4159-b4bc-1531388ecb40)

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/9c8c0bb6-9d13-43aa-86fa-94604b59b76d)

* Finally, graphs were plotted with the characters extracted from all 7 books using NetworkX and Pyvis.

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/f4aff0fe-e3bb-445f-9a6e-583f3af3e8e1)

![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/9bdf4cc2-ef67-41a0-9dc9-8cdac44a490c)




