 #Adrien Paysant Edouard Goffinet
 # Sources : 
 # https://github.com/jamesroutley/write-a-hash-table
 # https://www.tutorialspoint.com/cryptography/cryptography_hash_functions.htm
 # https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
 # https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/
 # https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/

 
class StorageNode:
	""" storage node data structure to be handled with Hashtable"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None


class HashTable:
	""" HashTable with separate chaining"""
	def __init__(self):
		self.capacity = 1000000
		self.size = 0
		self.squares = [None]*self.capacity

	def hash(self, key):
		""" hash the key value & return her index in storage """
		hashsum = 0
		for idx, c in enumerate(key):
			hashsum += (idx + len(key)) ** ord(c)
			hashsum = hashsum % self.capacity
		return hashsum

	def insert(self, key, value):
		""" insert couple key/value in hash table """
		self.size += 1
		index = self.hash(key)
		sNode = self.squares[index]
		if sNode is None:
			self.squares[index] = StorageNode(key, value)
			return
		prev = sNode
		while sNode is not None:
			prev = sNode
			sNode = sNode.next
		prev.next = StorageNode(key, value)

	def find(self, key):
		""" return data value based on the given key """
		index = self.hash(key)
		sNode = self.squares[index]
		while sNode is not None and sNode.key != key:
			sNode = sNode.next
		if sNode is None:
			return None
		else:
			return sNode.value

	def remove(self, key):
		""" remove a store key from the hash table & return removed value"""
		index = self.hash(key)
		sNode = self.squares[index]
		prev = None
		while sNode is not None and sNode.key != key:
			prev = sNode
			sNode = sNode.next
		if sNode is None:
			return None
		else:
			self.size -= 1
			result = sNode.value
			if prev is None:
				self.squares[index] = sNode.next
			else:
				prev.next = prev.next.next 
			return result

#######TESTS######

def hashTest():
	#hash test
	print("Processing hash tests...")
	hashTable= HashTable()
	print("Few examples : ")
	print("Hashing 'hearc' : "+str(hashTable.hash("hearc")))
	print("Hashing 'hearc' : "+str(hashTable.hash("hearc")))
	print("Hashing 'hearc2' : "+str(hashTable.hash("hearc2")))
	print("Hashing 'vjksldhbvjkldzsvbsdjhbvdsjkhbv' : "+str(hashTable.hash("vjksldhbvjkldzsvbsdjhbvdsjkhbv")))


	if(hashTable.hash("hearc")==hashTable.hash("hearc")):
		print("Hash Test Passed ! ")
	else:
		print("Hash Test Failled ! ")

def insertTest():
	#insert test
	print("Processing insert tests...")
	hashTable= HashTable()
	if(hashTable.size!=0):
		print("Error insert test")
		exit
	hashTable.insert("test_key", "test_value")
	if(hashTable.size!=1):
		print("Error insert test")
		exit
	if(hashTable.squares[hashTable.hash("test_key")].value=="test_value"):
		print("Insert Test Passed ! ")

def findTest():
	#find test
	print("Processing find tests...")
	hashTable= HashTable()
	if(hashTable.size!=0):
		print("Error Find Test")
		exit
	var="hearc"
	hashTable.insert("key1",var)
	if(var!=hashTable.find("key1")):
		print("Error Find Test")
		exit
	var=["hearc","Adrien","Edouard"]
	hashTable.insert("key2",var)
	if(var!=hashTable.find("key2")):
		print("Error Find Test")
		exit
	print("Find Tests Passed !")

def removeTest():
	#remove test
	print("Processing remove tests...")
	hashTable= HashTable()
	if(hashTable.size!=0):
		print("Error Remove Test")
		exit
	var="hearc"
	hashTable.insert("key1",var)
	if(hashTable.size!=1):
		print("Error Remove Test")
		exit
	if(var!=hashTable.remove("key1")):
		print("Error Remove Test")
		exit
	if(hashTable.size!=0):
		print("Error Remove Test")
		exit
	if(None!=hashTable.remove("RANDOM")):
		print("Error Remove Test")
		exit
	print("Remove Tests Passed ! ")

def loadTest(size):
	#load test
	print("Processing load tests...")
	hashTable=HashTable()
	for i in range(0,size):
		if(hashTable.size!=i):
			print("Error Load Test")
			exit
		hashTable.insert("key" + str(i), "hearc")
	if(hashTable.size!=size):
			print("Error Load Test")
			exit
	for i in range(0,size):
		if(hashTable.size!=size-i):
			print("Error Load Test")
			exit
		if(hashTable.find("key"+str(i))!=hashTable.remove("key"+str(i))):
			print("Error Load Test4")
			exit
	print("Load Tests Passed ! ")

if __name__=="__main__":
	print("HASHES - Tests")
	print("Beginning Test ...")
	print("")
	hashTest()
	print("")
	insertTest()
	print("")
	findTest()
	print("")
	removeTest()
	print("")
	loadTest(100) #Takes approximatly 25 seconds with 100000
	print("")
	print("End Tests")
	print("End Demo")
