class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"{self.data}"


class Stack:

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        return f"{self.head}"

    def push(self, data: str):
        """
        Add an item in the stack.

        :param data: input data
        """
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        Remove an item from the stack.
        :return: Return popped element
        """
        self.empty_check()
        temp = self.head.data
        self.head = self.head.next
        return str(temp)

    def peek(self):
        """
        :return: Return the top element of the stack.
        """
        self.empty_check()
        return str(self.head)

    def is_empty(self):
        """
        :return: Return true if the stack is empty, else false.
        """
        if not self.head:
            return True
        return False

    def size(self):
        """
        :return: Return the size of the stack.
        """
        if self.is_empty():
            return "0"
        counter = 1
        curr = self.head
        while curr.next is not None:
            counter += 1
            curr = curr.next
        return counter

    def print(self):
        """
        Return all elements in stack.
        """
        self.empty_check()
        curr = self.head
        elements = ""
        while curr is not None:
            elements += curr.data
            curr = curr.next
        return elements[::-1]

    def empty_check(self):
        if self.is_empty():
            return "Error: Stack Empty"


def inflix_parse(inflix: str) -> list:
    """
    infix converts the expression from str format to a list format.
    :param inflix: A variable in the stack structure
    :return: Converted infix expression to list format
    """
    inflix_list = []
    temp = ""
    while inflix:
        if not inflix[0].isdigit():
            if temp:
                inflix_list.append(temp)
                temp = ""
            inflix_list.append(inflix[0])
            inflix = inflix[1:]
        else:
            temp += inflix[0]
            inflix = inflix[1:]

    if temp:
        inflix_list.append(temp)
    return inflix_list


def inflix_to_postfix(inflix: str) -> Stack:
    """
    Converts inflix expression to postfix expression
    :param inflix: A variable in the stack structure
    """
    inflix = inflix_parse(inflix)

    operators = Stack()
    postfix = Stack()

    for i in inflix:

        if i.isdigit():
            postfix.push(i)

        if i in ("+", "-"):
            if (operators.peek()) in ("+", "-", "*", "/"):
                postfix.push(operators.pop())

                if (operators.peek()) in ("+", "-"):
                    postfix.push(operators.pop())
            operators.push(i)

        if i in ("/", "*"):
            if (operators.peek()) in ("*", "/"):
                postfix.push(operators.pop())
            operators.push(i)

        if i == "(":
            operators.push(i)

        if i == ")":
            while operators.peek() != "(":
                postfix.push(operators.pop())
            operators.pop()

    # if last element in operators is not ")" there is one miss element in operators
    if not operators.is_empty():
        postfix.push(operators.pop())

    print("Postfix expression:", postfix.print())
    return postfix


def reverse_stack(stack: Stack) -> Stack:
    """
    reverses the stack
    :param stack: A variable in the stack structure
    :return: Returns a stack opposite the stack it takes as a variable
    """
    reverse_postfix = Stack()
    while not stack.is_empty():
        reverse_postfix.push(stack.pop())
    return reverse_postfix


def postflix_to_solition(postfix: Stack):
    """
    Postfix prints the result of an expression to the screen
    :param postfix: A variable in the stack structure

    """
    solition_stack = Stack()
    reverse_postfix = reverse_stack(stack=postfix)

    while not reverse_postfix.is_empty():
        if reverse_postfix.peek() in ("+", "-", "*", "/"):
            operator = reverse_postfix.pop()
            first_pop = float(solition_stack.pop())
            second_pop = float(solition_stack.pop())

            if operator == "+":
                result = second_pop + first_pop
            if operator == "-":
                result = second_pop - first_pop
            if operator == "*":
                result = second_pop * first_pop
            if operator == "/":
                result = second_pop / first_pop

            solition_stack.push(result)
        else:
            solition_stack.push(reverse_postfix.pop())

    print("Value =", result)


postflix_to_solition(inflix_to_postfix("(1+(6/2)*(1+9)-1)"))
