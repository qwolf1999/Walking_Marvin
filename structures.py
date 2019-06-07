from enum import Enum
from typing import Dict, List
import copy

class Edge:
	start = -1
	end = -1
	def __copy__(self):
		e = Edge()
		e.start = self.start
		e.end = self.end
		return e

class Link:
	innovation_num = -1
	path = Edge()
	weight = 0.0
	enabled = True
	def __str__(self):
		return(f"{self.weight}\n     {self.path.start}\t-> {self.path.end}\n")

class NodeType(Enum):
	NONE = 0
	INPUT = 1
	OUTPUT = 2
	BIAS = 3
	HIDDEN = 4

class Node:
	nid = -1
	nodeType = NodeType.NONE

class Individual:
	nodes = []
	links = []
	def __copy__(self):
		i = Individual()
		i.nodes = copy.deepcopy(self.nodes)
		i.links = [] #not copying links.
		#i.links = copy.deepcopy(self.links)
		return i

class Global:
	individuals = []
	innovations = {}
	nInput = 0
	nOutput = 0
	nNodes = 0
	nGen = 1
	env = 0
	def NewNode(self, nodeType: NodeType):
		node = Node()
		node.nid = self.nNodes
		node.nodeType = nodeType
		self.nNodes += 1
		return node
	def GetInnovationNum(self, edge: Edge):
		if not edge in self.innovations:
			self.innovations[edge] = len(self.innovations)
		return self.innovations[edge]
