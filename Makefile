#Script to execute the project

PLOT_SRC = scripts/main.py
LANGUAGE =python
PLOT_EXE=$(LANGUAGE) $(PLOT_SRC)
TXT_FILE=data/9606.protein.links.v11.0.txt
PNG_FILE=protein_domains_vs_string_degree.png

plot:
	$(PLOT_EXE) $(TXT_FILE) $(PNG_FILE)
