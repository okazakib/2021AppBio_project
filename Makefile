#Script to execute the project

PLOT_SRC = scripts/main.py
LANGUAGE =python
PLOT_EXE=$(LANGUAGE) $(PLOT_SRC)

#COMPRESSED_TXT_FILE=data/9606.protein.links.v11.0.txt.gz
#TXT_FILE=data/9606.protein.links.v11.0.txt

PNG_FILE=protein_domains_vs_string_degree.png

all:myensembldb.txt plot clean

myensembldb.txt:
	curl -L https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz | gunzip > $@
		
plot:
        $(PLOT_EXE) myensembldb.txt $(PNG_FILE)

clean:
        rm myensembldb.txt
		
	

