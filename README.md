
## Research Areas Analysis Using Graph Data and Large Language Models
### Donato Riccio

![](image-1.png)


This project involves an in-depth analysis of research areas, particularly focusing on how research in machine learning has evolved over time. By leveraging a large dataset of citation networks, the project aims to identify and analyze trends within different research communities.

### Dataset
The dataset used for this analysis is sourced from Kaggle and can be found here: [Citation Network Dataset](https://www.kaggle.com/datasets/mathurinache/citation-network-dataset).

### Repository Contents
This repository includes several key files, each serving a specific purpose in the analysis:

1. **0-csv-conversion.ipynb**: This notebook handles the conversion and filtering of data from JSON to CSV format, setting up the dataset for further analysis.
2. **1-graph_building.ipynb**: This notebook contains the code for constructing the citation graph, calculating partitions using the Infomap algorithm, and determining HITS scores.
3. **2-research_analysis.ipynb**: The core notebook of the project. It presents the results of the research area analysis, identifying trends and evolutions over time.
4. **2-research_analysis.html**: Exported notebook without source code for easier reading.
5. **utils.py**: Supporting functions and prompt.

### Project Goals
The primary objective of this project is to partition the citation graph into communities. These communities are interpreted as different research areas, which are then analyzed to identify trending topics and understand the evolution of research in the field of machine learning.

### Technical Details
- **Graph Construction**: The citation network graph constructed in this project comprises over 3 million nodes.
- **Scalability**: The analysis includes various optimization tricks to handle such a large dataset efficiently, allowing the computations to be run on a MacBook Pro with 18GB of RAM.

### Future steps
- **Recommendation system**  
- **Q&A with RAG**

By partitioning the graph into distinct research communities, the project aims to provide insights into which areas are gaining prominence and how research directions have shifted over time.
