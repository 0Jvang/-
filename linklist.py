class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkList:
	"""
	考虑三种情况：
	1. 链表为空
	2. 链表不为空，头部操作
	3. 链表不为空，中间操作
	"""
	def __init__(self):
		self.__head = None

	def __getitem__(self, index):
		if index < 0 or self.__head is None:
			raise IndexError

		count = 0
		node = self.__head
		for i in range(index):
			node = node.next
			count += 1

			if node is None:
				raise IndexError
		return node

	def __iter__(self):
		node = self.__head
		while node:
			yield node
			node = node.next

	def insert(self, index, value):
		new_node = Node(value)

		if self.__head is None:
			self.__head = new_node
			return

		if index <= 0:
			new_node.next = self.__head
			self.__head = new_node
			return

		count = 0
		node = self.__head
		# 迭代链表获得index前一位或最后一位的node	
		while count < index - 1 and node.next:
			node = node.next
			count += 1

		new_node.next = node.next
		node.next = new_node

		print(f'insert -> index:{index} value:{value}')

	def delete(self, index):
		if self.__head is None:
			return

		if index <= 0 or self.__head.next is None:
			self.__head = self.__head.next
			return

		# 到这里链表至少有两个元素
		count = 0
		node = self.__head
		# 迭代链表获得index前一位node, 如index超出链表长度则获得为倒数第二位node
		while count < index - 1 and node.next.next:
			node = node.next
			count += 1

		node.next = node.next.next

		print(f'delete -> index:{index}')

	def update(self, index, value):
		self[index].value = value


def test():
	link_list = LinkList()
	link_list.insert(-1, -1)
	link_list.insert(0, 0)
	link_list.insert(999, 999)
	link_list.insert(2, 2)
	link_list.insert(3, 3)
	test_iter(link_list)

	for i in range(5):
		print(link_list[i].value)
	link_list.update(0, '零')
	test_iter(link_list)

	link_list.delete(0)
	test_iter(link_list)
	link_list.delete(-1)
	test_iter(link_list)
	link_list.delete(2)
	test_iter(link_list)
	link_list.delete(999)
	test_iter(link_list)
	link_list.delete(0)
	test_iter(link_list)
	link_list.delete(999)
	test_iter(link_list)
	link_list.delete(999)
	test_iter(link_list)
	link_list.delete(-1)
	link_list.delete(0)
	test_iter(link_list)


def test_iter(link_list):
	print(' -> '.join([str(node.value) for node in link_list]))

if __name__ == '__main__':
	test()