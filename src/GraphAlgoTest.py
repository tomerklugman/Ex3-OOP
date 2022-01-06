import unittest
from GraphAlgo import *


class GraphAlgoTest(unittest.TestCase):

    def test_get_graph(self):
        a = DiGraph()
        a.add_node(1)
        a.add_node(2)
        a.add_node(3)
        a.add_node(4)
        algo=GraphAlgo(a)

        self.assertEqual(algo.get_graph(), a)

    def test_load_from_json(self):
        algo=GraphAlgo()
        algo.load_from_json("../data/A5.json") #load file
        a = algo.get_graph() #get graph will get it loaded succesfully

        self.assertEqual(algo.get_graph(), a)

    def test_save_to_json(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/A5.json") # load file
        a = algo.get_graph() # save it at a
        algo.save_to_json("../data/A5.json" + '_saved') # create "saved" file
        algo.load_from_json("../data/A5.json_saved") # load it to algo

        self.assertEqual(algo.get_graph(), a) # check if both graphs equal then saved succesfully

    def test_shortest_path(self): # and dijkstras algorithm check
        algo = GraphAlgo()
        algo.load_from_json("../data/A5.json") # load file
        dist, path = algo.shortest_path(1, 7)
        self.assertEqual(dist, 2.062180280059253)
        self.assertEqual(path, [1, 10, 7])

    def test_TSP(self):
        algo = GraphAlgo()
        algo.load_from_json("../data/A5.json") # load file

        path, dist =algo.TSP([1, 2, 3])

        self.assertEqual(dist, 2.370613295323088)
        self.assertEqual(path, [1, 9, 2, 3])

    def test_centerPoint(self): # and isConnected check
        algo = GraphAlgo()
        algo.load_from_json("../data/A5.json") # load file

        node, dist=algo.centerPoint()

        self.assertEqual(node, 40)
        self.assertEqual(dist, 9.291743173960954)

        a = DiGraph()
        a.add_node(1)
        a.add_node(2)
        b=GraphAlgo(a)
        self.assertEqual(b.centerPoint(),(None, float('inf'))) # not connected/cant reach all nodes/ dist between nodes is inf

        a.add_edge(1, 2, 1)
        a.add_edge(2, 1, 1)
        self.assertEqual(b.centerPoint(),(1, 1)) # connected
