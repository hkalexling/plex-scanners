import re

class UfcFightNightAgent(object):
  def get_regex(self):
    return re.compile('^ufc.fight.night', re.IGNORECASE)

  def __init__(self, log):
    if log is None:
      self.log = Log
    else:
      self.log = log

  def getShowMetadata(self, title):
    return {
      'poster': 'ufc-poster.jpg',
      'background': 'ufc-background.jpg'
    }

  def getSeasonMetadata(self, title, season):
    return {
      'poster': 'ufc-poster.jpg',
    }

  PARTS = {
    1: "Early Prelims",
    2: "Prelims",
    3: "Main Event",
  }

  def getEpisodeMetadata(self, title, season, episode):
    ep = int(episode)
    part = ep % 10
    title = self.PARTS[part]

    return {
      'thumb': 'ufc-poster.jpg',
      'title': title,
      'summary': '',
    }

def Log(str):
  print str
