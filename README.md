### Character Analysis of Harry Potter books using Spacy

**Aim:**
* Main goal of this project is to identify the main characters in the books and analyse the strength of relationship that exists between them.
* Libraries used would include Spacy, NetworkX, Pyvis.

  **Steps:**
  * Character names from all the 7 Harry potter books was obtained through a small web scraping project and preprocessing was done.
  * NER was extracted from all books and filtered out so that we have only names from the web scraped file.
  * Names from each 10 sentences were taken (window_size = 10) and grouped together to get a dataframe which shows the strength of relationship between two characters.
  * Graphs were created to visualize the extracted relationships.

**Inferences:**
* Strongest relationship was seen for the below characters.
![image](https://github.com/sruthi004/Character-Analysis-of-Harry-Potter-books-using-Spacy/assets/98512121/fd555d01-84f3-431c-8155-af4552927116)

