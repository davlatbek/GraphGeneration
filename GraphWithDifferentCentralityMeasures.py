import networkx as nx
import operator
import pylab

def distinct_centrality_nodes():
    while True:
        listofnodes_with_highest_centralities = []
        G = nx.erdos_renyi_graph(7, 0.1)
        degreelist = {}
        for i in G.nodes():
            degreelist[i] = G.degree(i)

        highestdegreecentrality = max(degreelist.iteritems(), key = operator.itemgetter((1)))[0]
        if max_centrality_within_metric_is_unique(degreelist[highestdegreecentrality], degreelist):
            listofnodes_with_highest_centralities.append(highestdegreecentrality)
        else:
            continue

        harmoniccentrality = nx.harmonic_centrality(G)
        highestharmonic = max(harmoniccentrality.iteritems(), key = operator.itemgetter((1)))[0]
        if max_centrality_within_metric_is_unique(harmoniccentrality[highestharmonic], harmoniccentrality):
            listofnodes_with_highest_centralities.append(highestharmonic)
        else:
            continue

        if (max_centrality_size_are_different(listofnodes_with_highest_centralities)):
            continue

        betweennesscentrality = nx.betweenness_centrality(G, normalized=True)
        highestbetweenness = max(betweennesscentrality.iteritems(), key = operator.itemgetter((1)))[0]
        if max_centrality_within_metric_is_unique(betweennesscentrality[highestbetweenness], betweennesscentrality):
            listofnodes_with_highest_centralities.append(highestbetweenness)
        else:
            continue

        if (max_centrality_size_are_different(listofnodes_with_highest_centralities)):
            continue

        eigenvectorcentrality = nx.eigenvector_centrality(G, max_iter=1000)
        highesteigenvector = max(eigenvectorcentrality.iteritems(), key = operator.itemgetter((1)))[0]
        if max_centrality_within_metric_is_unique(eigenvectorcentrality[highesteigenvector], eigenvectorcentrality):
            listofnodes_with_highest_centralities.append(highesteigenvector)
        else:
            continue

        if not (max_centrality_size_are_different(listofnodes_with_highest_centralities)):

            print "Number of nodes: ", G.number_of_nodes()
            print "Number of edges: ", G.number_of_edges()

            for k,v in degreelist.iteritems():
                print "node: ", k, " degree centrality: ", v
            print "node with the highest degree centrality :", highestdegreecentrality, "\n"

            for k,v in betweennesscentrality.iteritems():
                print "node: ", k, " betweenness centrality: ", round(v, 2)
            print "node with the highest betweenness centrality :", highestbetweenness

            for k,v in harmoniccentrality.iteritems():
                print "node: ", k, " harmonic centrality: ", round(v, 2)
            print "node with the highest harmonic: ", highestharmonic

            for k,v in eigenvectorcentrality.iteritems():
                print "node: ", k, " eigenvector centrality: ", round(v, 2)
            print "node with the highest eigenvector: ", highesteigenvector

            position = nx.spring_layout(G)
            nx.draw(G, position, with_labels=True)
            pylab.show()

            return

        else:
            continue

def max_centrality_size_are_different(list):
    if (len(list) != len(set(list))):
        return True

def max_centrality_within_metric_is_unique(elem, dict):
    count = 0
    for k,v in dict.iteritems():
        if (elem == v):
            count += 1
    if (count == 1):
        return True
    else:
        return False

distinct_centrality_nodes()