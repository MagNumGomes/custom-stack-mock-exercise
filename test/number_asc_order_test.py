import pytest
from src.custom_stack_class import CustomStack, StackEmptyException
from src.number_asc_order import NumberAscOrder


def test_sort_six_random_numbers_with_mock(mocker):
    numeros_sorteados = [53, 10, 4, 32, 27, 1]
    mock_stack = mocker.MagicMock(spec=CustomStack)
    mock_stack.is_empty.side_effect = [False, False, False, False, False, False, True]
    mock_stack.pop.side_effect = numeros_sorteados

    sorter = NumberAscOrder()
    resultado = sorter.sort(mock_stack)

    assert isinstance(resultado, list)
    assert len(resultado) == 6
    assert resultado == sorted(numeros_sorteados)
    assert resultado == [1, 4, 10, 27, 32, 53]
    assert mock_stack.pop.call_count == 6


def test_sort_empty_stack_with_mock(mocker):
    mock_stack = mocker.MagicMock(spec=CustomStack)
    mock_stack.is_empty.return_value = True

    sorter = NumberAscOrder()
    resultado = sorter.sort(mock_stack)

    assert resultado == []
    mock_stack.is_empty.assert_called_once()
    mock_stack.pop.assert_not_called()


def test_sort_with_none_raises_type_error():
    sorter = NumberAscOrder()

    with pytest.raises(TypeError):
        sorter.sort(None)


def test_sort_with_invalid_object_raises_type_error():
    sorter = NumberAscOrder()

    with pytest.raises(TypeError):
        sorter.sort([10, 20, 30])


def test_sort_propagates_stack_empty_exception_when_pop_fails(mocker):
    mock_stack = mocker.MagicMock(spec=CustomStack)
    mock_stack.is_empty.side_effect = [False, False]
    mock_stack.pop.side_effect = StackEmptyException()

    sorter = NumberAscOrder()

    with pytest.raises(StackEmptyException):
        sorter.sort(mock_stack)
