# -*- coding: utf-8 -*-

import tempfile
from nwdiag.builder import *
from nwdiag.elements import *
from nwdiag.diagparser import *


def __build_diagram(filename):
    import os
    testdir = os.path.dirname(__file__)
    pathname = "%s/diagrams/%s" % (testdir, filename)

    str = open(pathname).read()
    tree = parse(tokenize(str))
    return ScreenNodeBuilder.build(tree)


def test_diagram_attributes():
    screen = __build_diagram('diagram_attributes.diag')

    assert screen.node_width == 160
    assert screen.node_height == 160
    assert screen.span_width == 32
    assert screen.span_height == 32
    assert screen.fontsize == 16


def test_node_attributes():
    screen = __build_diagram('node_attributes.diag')

    network = screen.networks[0]
    assert screen.nodes[0].address[network] == '192.168.0.1'
    assert screen.nodes[1].address[network] == '192.168.0.2\n192.168.0.3'


def test_node_address_attribute():
    screen = __build_diagram('node_address_attribute.diag')

    network = screen.networks[0]
    assert screen.nodes[0].address[network] == '192.168.0.1'
    assert screen.nodes[1].address[network] == \
           '2001:0db8:bd05:01d2:288a:1fc0:0001:10ee'


def test_node_including_hyphen_diagram():
    screen = __build_diagram('node_including_hyphen.diag')

    network = screen.networks[0]
    assert screen.nodes[0].id == 'web-01'
    assert screen.nodes[1].id == 'web-02'


def test_single_network_diagram():
    screen = __build_diagram('single_network.diag')

    assert len(screen.nodes) == 1
    assert len(screen.networks) == 1
    assert screen.nodes[0].label == 'A'
    assert screen.nodes[0].xy == (0, 0)


def test_two_networks_diagram():
    screen = __build_diagram('two_networks.diag')

    assert_pos = {'A': (0, 0), 'B': (0, 1)}
    for node in screen.nodes:
        print assert_pos[node.id], node.xy
        assert node.xy == assert_pos[node.id]


def test_connected_networks_diagram():
    screen = __build_diagram('connected_networks.diag')

    assert_pos = {'A': (0, 0), 'B': (1, 1)}
    for node in screen.nodes:
        print assert_pos[node.id], node.xy
        assert node.xy == assert_pos[node.id]


def test_group_inner_network_diagram():
    screen = __build_diagram('group_inner_network.diag')

    assert_pos = {'A': (0, 0), 'B': (1, 0)}
    for node in screen.nodes:
        print assert_pos[node.id], node.xy
        assert node.xy == assert_pos[node.id]

    assert len(screen.groups[0].nodes) == 2
    assert screen.groups[0].width == 2
    assert screen.groups[0].height == 1


def test_group_outer_network_diagram():
    screen = __build_diagram('group_outer_network.diag')

    assert_pos = {'A': (0, 0), 'B': (1, 0)}
    for node in screen.nodes:
        print assert_pos[node.id], node.xy
        assert node.xy == assert_pos[node.id]

    assert len(screen.groups[0].nodes) == 2
    assert screen.groups[0].width == 2
    assert screen.groups[0].height == 1


def test_group_across_network_diagram():
    screen = __build_diagram('group_across_network.diag')

    assert_pos = {'A': (0, 0), 'B': (1, 0), 'C': (2, 1)}
    for node in screen.nodes:
        print assert_pos[node.id], node.xy
        assert node.xy == assert_pos[node.id]

    assert len(screen.groups[0].nodes) == 3
    assert screen.groups[0].width == 3
    assert screen.groups[0].height == 2