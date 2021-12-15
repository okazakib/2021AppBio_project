#!/usr/bin/python

##Author: Nayanika Bhalla
##Description:
##Usage:main.py <input_file> <output_file>

#####################################################

exec(open('scripts/src.py').read())
import sys

#args = sys.argv[1:]

def main():
    ###Read the provided text file containing the information about different protein interactions as a dataframe.
    #network_dataframe = pd.read_csv('./data/9606.protein.links.v11.0.txt', sep=' ')

    network_dataframe= pd.read_csv(sys.argv[1],sep=' ')
    output_file=sys.argv[2]

    network_dataframe_filtered=filter_score_df(network_dataframe)
    network_dataframe_renamed=rename_proteins(network_dataframe_filtered)
    network=add_edges(network_dataframe_renamed)

    ###Read the file containing information about known protein-domains per Ensembl id as a dataframe
    protein_domains=pd.read_csv('./data/proteins_w_domains.txt', sep='\t')

    comb_network_greater=create_degree_greater_dataframe(network,protein_domains)
    comb_network_lesser=create_degree_lesser_dataframe(network,protein_domains)

    ###Create the boxplot
    create_boxplot(comb_network_greater,comb_network_lesser)
    plt.savefig(output_file)
    return 0

if __name__ == "__main__":
    main()
