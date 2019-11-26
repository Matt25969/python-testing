import pytest
from applications import count

def test_count_zeros():
	assert count.count([0,0,0],0)==5

def test_count_string():
	assert count.count(["a","a","a"],"a")==3

def test_count_minus():
	assert count.count([-1,-3,-5,-4], -1)==1
