import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_push_one_elementinstack():
    element_value = 5.0

    cut = CustomStack(5)
    assert cut.is_empty() is True
    assert cut.size() == 0

    cut.push(element_value)
    assert cut.is_empty() is False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_push_multiple_elements_within_limit():
    cut = CustomStack(3)
    cut.push(10)
    cut.push(20)
    cut.push(30)

    assert cut.is_empty() is False
    assert cut.size() == 3
    assert cut.top() == 30


def test_push_when_stack_is_full_raises_exception():
    cut = CustomStack(2)
    cut.push(10)
    cut.push(20)

    with pytest.raises(StackFullException):
        cut.push(30)

    assert cut.size() == 2
    assert cut.top() == 20


def test_pop_returns_top_element_and_decreases_size():
    cut = CustomStack(3)
    cut.push(10)
    cut.push(20)

    popped = cut.pop()
    assert popped == 20
    assert cut.size() == 1
    assert cut.top() == 10
    assert cut.is_empty() is False

    last_popped = cut.pop()
    assert last_popped == 10
    assert cut.size() == 0
    assert cut.is_empty() is True


def test_pop_when_stack_is_empty_raises_exception():
    cut = CustomStack(5)
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.pop()


def test_top_when_stack_is_empty_raises_exception():
    cut = CustomStack(5)
    assert cut.is_empty() is True

    with pytest.raises(StackEmptyException):
        cut.top()
