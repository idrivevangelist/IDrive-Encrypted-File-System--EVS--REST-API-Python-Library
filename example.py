<%
import sys
sys.path.append("/var/www/html/working")
import IDrive
from xml.dom.minidom import parseString
import xml.dom.minidom as xdm

#create an instance of the library
myNewObj = IDrive.IDrive('<IDRIVE UID>', '<IDRIVE PWD>')

#create the parameters dictionary
inparams = {}

#load the server response into a variable
result = myNewObj.execute('validateAccount', inparams)

#parse the XML response
dom = xdm.parseString(result)
root = dom.documentElement
atr1 = root.getAttributeNode('message')

#print the response
%>
<strong>Valiate Account</strong></br />
<%=atr1.nodeValue%>
<%
inparams = {}
inparams['pvtkey'] = ""
inparams['enctype'] = "default"
result = myNewObj.execute('configureAccount', inparams)

dom = xdm.parseString(result)
root = dom.documentElement
atr2 = root.getAttributeNode('message')
%>
<br /><strong>Configure Account</strong></br />
<%=atr2.nodeValue%>
<%
inparams = {}
inparams['p'] = "/OWNER-PC"
inparams['searchkey'] = "Crysanthemums"
inparams['trash'] = "yes"
result = myNewObj.execute('searchFiles', inparams)

dom = xdm.parseString(result)
root = dom.documentElement
atr2 = root.getAttributeNode('message')
%>
<br /><strong>Search Files</strong></br />
<%=atr2.nodeValue%>
<%
inparams = {}
result = myNewObj.execute('getAccountQuota', inparams)

dom = xdm.parseString(result)
root = dom.documentElement
atr2 = root.getAttributeNode('message')
%>
<br /><strong>Get Account Quota</strong></br />
<%=atr2.nodeValue%>
