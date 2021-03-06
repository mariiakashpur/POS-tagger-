from Evaluation import Evaluation
from Corpus import Corpus

class Training(object):
  def __init__(self, algorithm): # algorithm is instance of any algorithm class, e.g. MCP
    self.algorithm = algorithm

  def train(self, numIterations=100, testCorpusPath=None):
    if testCorpusPath:
      testCorpus = Corpus(testCorpusPath)
    for i in range(1, numIterations + 1):
      self.algorithm.train() # call train method from algorithm
      if i % 10 == 0:
        # trainEval = Evaluation(self.algorithm.corpus)
        # print "Training evaluation for", i, "iteration(s):\n", trainEval.format()
        # self.algorithm.corpus.resetSentStats()
        if testCorpusPath:
          self.setPredictedTags(testCorpus) 
          testEval = Evaluation(testCorpus)
          print "Testing evaluation for", i, "iteration(s):\n",testEval.format()
          testCorpus.resetSentStats() # !!! we can use prototype pattern(so we don't need to loop through sents): here testCorpus = testCorpus.getPrototype() and in Corpus::__init__ : self.prototype = self (google : python prototype)?
          # if i == numIterations:
          #   testEval.mistagedTokens()

  def setPredictedTags(self, testCorpus):
    for sent in testCorpus.getSents():
      for token in sent.getTokens():
        predictedTag = self.algorithm.getBestTag(token) # !!! we get best tags for tag and then update predicted tags for this token, why not to make in one line?
        token.setPredictedPOS(predictedTag)


      

  # def predict(self, corpus):
  #   predictions = []
  #   for sent in corpus.getSents():
  #     sentTokens = []
  #     for token in sent.getTokens():
  #       sentTokens.append({token.getText(): self.algorithm.getBestTag(token)})
  #     predictions.append(sentTokens)
  #   return predictions

  # def createOutputFile(self, predictions, predictedPath):
  #   with open(predictedPath, "w") as f:
  #     for sent in predictions:
  #       for token in sent:
  #         f.write(str(token.keys()[0]) + "\t" + str(token.values()[0]) + "\n")
  #       f.write("\n")
