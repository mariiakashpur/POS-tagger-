from collections import defaultdict


class Sentence(object):
  def __init__(self):
    self.tokens = []
    self.token_stats = {}
    self.sentText = []

  def addToken(self, token):
    self.tokens.append(token)

  def getTokens(self):
  	return self.tokens

  def getSentText(self): # !!! why not init sentence obj with line from a file, so there is no need in join token text @see Corpus::__init__()
    sentTokens = []
    for token in self.getTokens():
      sentTokens.append(token.getText())
    self.sentText = ' '.join(sentTokens)

    return self.sentText

  def getTokenStats(self):
    for token in self.getTokens(): # first iteration to collect all tags in both gold and predicted sent tagging
      gt = token.getGoldPOS()
      pt = token.getPredictedPOS()
      if not gt in self.token_stats:
        self.token_stats[gt] = {"TP":0, "FP":0, "FN":0}
      if not pt in self.token_stats:
        self.token_stats[pt] = {"TP":0, "FP":0, "FN":0}
    # !!! why do we need two for loops, put all in one
    # for token in self.getTokens(): # first iteration to collect all tags in both gold and predicted sent tagging
    #   gt = token.getGoldPOS()
    #   pt = token.getPredictedPOS()
    #   if not gt in self.token_stats:
    #     self.token_stats[gt] = {"TP":0, "FP":0, "FN":0}
    #   if not pt in self.token_stats:
    #     self.token_stats[pt] = {"TP":0, "FP":0, "FN":0}
    #   if token.isLabeledCorrectly():
    #     self.token_stats[gt]["TP"] += 1 # tags coincide
    #   else:
    #     self.token_stats[gt]["FN"] += 1 # increment FN counter for gold tag
    #     self.token_stats[pt]["FP"] += 1 # increment FP counter for predicted tag
    for token in self.getTokens():
      gt = token.getGoldPOS()
      pt = token.getPredictedPOS()
      if token.isLabeledCorrectly():
        self.token_stats[gt]["TP"] += 1 # tags coincide
      else:
        self.token_stats[gt]["FN"] += 1 # increment FN counter for gold tag
        self.token_stats[pt]["FP"] += 1 # increment FP counter for predicted tag
    return self.token_stats


  def resetTokenStats(self):
    self.token_stats = {}