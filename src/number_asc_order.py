from src.custom_stack_class import CustomStack


class NumberAscOrder:

    def sort(self, stack: CustomStack) -> list:
        if stack is None or not hasattr(stack, "is_empty") or not hasattr(stack, "pop"):
            raise TypeError("O parâmetro 'stack' deve ser uma instância válida de CustomStack.")

        if stack.is_empty():
            return []

        numbers = [stack.pop()]
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
