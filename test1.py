#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
# encoding=utf8
import py2neo
from py2neo import Graph, Path, authenticate, Node, Relationship



def createNodeWithLabelProperties():
    print ("Start - Connection to database")
    authenticate("localhost", "neo4j", "neo4j")
    graph = Graph("http://localhost/db/data/",http_port=32769,bolt_port=32768)
    print ("Creating nodes")
    node1 = Node ("Label1", name="Node1")
    node2 = Node ("Label1", "Label2", name="Node2")
    id1 = graph.create(node1)
    id2 = graph.create(node2)
    print ("End - Creating nodes with label and properties")
    r1 = Relationship(node1,"connected_to",node2, port=80)
    r2 = Relationship(node2, "connected_from", node1, port=6180)
    graph.create(r1)
    graph.create(r2)

if __name__ == '__main__':
    print ("Start Creating Nodes")
    createNodeWithLabelProperties()
    print ("End Creating Nodes")

