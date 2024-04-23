"""
These exercises focus on different approaches for writing property-based tests.

Try to find more than one test case for each exercise and test the functions under test extensively.
"""
import pytest
from hypothesis import given, strategies as st

# Exercise 1: Use Hypothesis to test the `reversed` built-in function for lists

@given(st.lists(st.integers() | st.floats() | st.text()))
def test_reversed(elements):
    rev_elems = list(reversed(elements))
    assert len(elements) == len(rev_elems)

    rev_rev_elems = list(reversed(rev_elems))
    assert elements == rev_rev_elems



# Exercise 2: Use Hypothesis to test the `sorted` built-in function for lists.

# NOTE: We can't use "@given(st.lists(st.integers() | st.floats() | st.text()))"
# because sorted() can't compare ints and strings.
@given(
    st.one_of(
        st.lists(st.integers()),
        st.lists(st.text()),
    )
)
def test_sorted(elements):
    sorted_elems = sorted(elements)
    if len(elements) == 0:
        assert sorted_elems == elements

    num_elems = len(elements)
    assert num_elems == len(sorted_elems)

    for i in range(num_elems - 1):
        assert sorted_elems[i+1] >= sorted_elems[i]



# Exercise 3: Use Hypothesis to test the `enumerate` built-in function for lists.

@given(st.lists(st.integers() | st.floats() | st.text()))
def test_enumerated(elements):
    enumerated_elements = list(enumerate(elements))
    assert enumerated_elements == [(i, elements[i]) for i in range(len(elements))]

