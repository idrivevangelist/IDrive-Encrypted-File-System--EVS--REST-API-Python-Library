import urllib, urllib2
from xml.dom.minidom import parseString
import xml.dom.minidom as xdm
class IDrive:
        Name = "IDrive"
        def __init__(self, uid, pwd):
                self.uid = uid
                self.pwd = pwd

                url = 'https://evs.idrive.com/evs/getServerAddress'
                print url
                self.uid = uid
                self.pwd = uid

                params = urllib.urlencode({
                        'uid': uid,
                        'pwd': pwd
                })
                print params
                result = urllib.urlopen(url, params).read()
                dom = xdm.parseString(result)
                root = dom.documentElement
                atr = root.getAttributeNode('webApiServer')
                print atr.nodeValue

                self.base_url = 'https://'+ atr.nodeValue

        def execute(self, page, parameters):
                url = self.base_url + '/evs/' + page
                print url
                parameters['uid'] = self.uid
                parameters['pwd'] = self.pwd

                params = urllib.urlencode(parameters)
                print params
                result = urllib.urlopen(url, params).read()
                return result

