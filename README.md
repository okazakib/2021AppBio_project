# 2021AppBio_project
Project for course Applied Bioinfromatics.

This project explore whether proteins with a high node-degree in protein interaction networks, also have a larger number of protein domains.

The instructions provided for the project were as follows:
1. Download the Homo sapiens part of STRING, a database from protein-protein interactions, from
https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz (Links to an external site.)
The link above is from their download page.
2. Create an interaction network by selecting the edges with a "combined score" larger or equal to 500, a number which indicates significance.
3. Partition the proteins in two groups, the ones with a node degree larger than 100 and one smaller or equal to 100.
4. Download the number of known protein-domains per Ensembl id from:
https://stockholmuniversity.box.com/s/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex
This file was exported from Ensembl's BioMart (Links to an external site.) service and contains two columns: Pfam ID (for protein domains) and Ensembl protein ID (which is also used by the string database). Note: some proteins have no protein domain registered.
5. Make a boxplot, comparing the number of domains of proteins with node degrees >100 to the ones with node degrees <=100.
