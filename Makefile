#Script to execute the project

PLOT_SRC = scripts/main.py
LANGUAGE =python
PLOT_EXE=$(LANGUAGE) $(PLOT_SRC)
#COMPRESSED_TXT_FILE=curl -L https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz -o data/9606.protein.links.v11.0.txt.gz
#TXT_FILE=data/9606.protein.links.v11.0.txt
PNG_FILE=protein_domains_vs_string_degree.png

TXT_FILE:
	curl -L https://stockholmuniversity.box.com/shared/static/n8l0l1b3tg32wrzg2ensg8dnt7oua8ex -o data/myensembldb.txt
	
#uncompress_file:
	#UNCOMPRESSED_TXT_FILE=gunzip $(COMPRESSED_TXT_FILE)

#UNCOMPRESSED_TXT_FILE= data/myensembldb.txt
#plot:
	#$(PLOT_EXE) $(UNCOMPRESSED_TXT_FILE) $(PNG_FILE)
	
plot:
	#$(PLOT_EXE) $(TXT_FILE) $(PNG_FILE)
