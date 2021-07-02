#Script to execute the project

PLOT_SRC = scripts/main.py
LANGUAGE =python
PLOT_EXE=$(LANGUAGE) $(PLOT_SRC)
COMPRESSED_TXT_FILE=data/9606.protein.links.v11.0.txt.gz
PNG_FILE=protein_domains_vs_string_degree.png

uncompress_file:
	UNCOMPRESSED_TXT_FILE=gzip $(COMPRESSED_TXT_FILE)
	
plot:
	$(PLOT_EXE) $(UNCOMPRESSED_TXT_FILE) $(PNG_FILE)
