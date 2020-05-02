import stockAnalytics
import liveGraph

test = stockAnalytics.create("TLSA")

graph = liveGraph.liveGraph(test.getStockLabel())
graph.graph()