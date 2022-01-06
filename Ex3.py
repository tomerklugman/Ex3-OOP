import sys

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


def run(file):
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    g_algo.plot_graph()


if __name__ == '__main__':  # change file name here A0-A5 and T0
    run("data/A5.json")
