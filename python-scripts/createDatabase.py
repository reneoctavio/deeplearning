from random import shuffle
import math

def getProperties(dir):
	file = open(dir + '/files.txt', 'r')

	images = []
	categories = []
	cat = ''
	catNum = 1

	for line in file:
		ln = line.split()
		path = ln[0]
		
		if cat != ln[1]:
			cat = ln[1]
			category = Category(cat, catNum)
			categories.append(category)
			catNum = catNum + 1

		image = Image(path, category)
		category.addImage(image)
		images.append(image)
	return categories, images

def shuffleImagePlaces(categories):
	for category in categories:
		shuffle(category.getImages())
	return categories
		
def createSets(categories, percTrain, percValid, percTest):
	trainSet = []
	validSet = []
	testSet = []
	
	for category in categories:
		images = category.getImages()
		if (percTrain == 100) and (percValid == 0) and (percTest == 0):
			trainSet.append(images)
		elif (percTrain != 100) and (percValid != 0) and (percTest == 0):
			assert (percTrain + percValid) == 100, "Sum is not 100%"
			trainEndIndex = int(math.floor(len(images) * percTrain / 100))
			trainSet.append(images[0:trainEndIndex])
			validSet.append(images[trainEndIndex:len(images)])
		elif (percTrain != 100) and (percValid == 0) and (percTest != 0):
			assert (percTrain + percTest) == 100, "Sum is not 100%"
			trainEndIndex = int(math.floor(len(images) * percTrain / 100))
			trainSet.append(images[0:trainEndIndex])
			testSet.append(images[trainEndIndex:len(images)])
		elif (percTrain != 100) and (percValid != 0) and (percTest != 0):
			assert (percTrain + percValid + percTest) == 100, "Sum is not 100%"
			trainEndIndex = int(math.floor(len(images) * percTrain / 100))
			validEndIndex = int(math.floor(len(images) * percValid / 100) + trainEndIndex)
			trainSet.append(images[0:trainEndIndex])
			validSet.append(images[trainEndIndex:validEndIndex])
			testSet.append(images[validEndIndex:len(images)])
		else:
			assert "Not valid percentages"
			
	return trainSet, validSet, testSet
	
def saveSetsFile(dir, trainSet, validSet, testSet):
	""" Save Train file """
	fileTrain = open(dir + '/trainset.txt', 'w')
	for images in trainSet:
		for image in images:
			fileTrain.write(image.getPath() + ' ' + str(image.getCategory().getCategoryNumber()) + '\n')
	fileTrain.close()
	
	""" Save Valid file """
	if len(validSet) != 0:
		fileValid = open(dir + '/validset.txt', 'w')
		for images in validSet:
			for image in images:
				fileValid.write(image.getPath() + ' ' + str(image.getCategory().getCategoryNumber()) + '\n')
		fileValid.close()
		
	""" Save Valid file """
	if len(testSet) != 0:
		fileTest = open(dir + '/testset.txt', 'w')
		for images in testSet:
			for image in images:
				fileTest.write(image.getPath() + ' ' + str(image.getCategory().getCategoryNumber()) + '\n')
		fileTest.close()

def saveCategoryFile(dir, categories):
	fileCat = open(dir + '/categories.txt', 'w')
	for cat in categories:
		fileCat.write(cat.getCategoryName() + ' ' + str(cat.getCategoryNumber()) + '\n')
	fileCat.close()
		

class Category:
	def __init__(self, category, catNumber):
		self.categoryName = category
		self.categoryNumber = catNumber
		self.images = []
		
	def getCategoryName(self):
		return self.categoryName
		
	def getCategoryNumber(self):
		return self.categoryNumber
		
	def getImages(self):
		return self.images
		
	def addImage(self, image):
		self.images.append(image)

class Image:
	def __init__(self, path, category):
		self.imagePath = path
		self.imageCategory = category
		
	def getPath(self):
		return self.imagePath
		
	def getCategory(self):
		return self.imageCategory
		

dir = '/Users/reneoctavio/Documents/TorchData/Caltech101/101_ObjectCategories'

categories, images = getProperties(dir)
categories = shuffleImagePlaces(categories)
trainSet, validSet, testSet = createSets(categories, 70, 20, 10)
saveSetsFile(dir, trainSet, validSet, testSet)
saveCategoryFile(dir, categories)