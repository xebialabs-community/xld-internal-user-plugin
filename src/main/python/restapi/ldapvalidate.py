from org.springframework.ldap.core import LdapTemplate
from org.springframework.ldap.core.support import LdapContextSource
from java.net import ConnectException
from java.net import SocketException
from org.springframework.ldap import CommunicationException
from org.springframework.ldap import NameNotFoundException
from org.springframework.ldap import AuthenticationException

lcontext = LdapContextSource()
lcontext.setUserDn(request.entity['managerDn'])
lcontext.setPassword(request.entity['managerPassword'])
lcontext.setBase(request.entity['userBase'])
lcontext.setUrls([request.entity['ldapURL']])

# This block test all the connectivity to LDAP
try:
  lcontext.afterPropertiesSet()
  lcontext.getReadOnlyContext()
except ConnectException, e:
  print  e.getMostSpecificCause()
except SocketException, e:
  print  e.getMostSpecificCause()
except AuthenticationException, e:
  print  e.getMostSpecificCause()  
except CommunicationException, e:
  print  e.getMostSpecificCause()

# This block validates the users
try:
  ltmpl = LdapTemplate(lcontext)
  ltmpl.lookup(request.entity['userDn'])
  print  "User found"
except NameNotFoundException, e:
  print  "User not found"
