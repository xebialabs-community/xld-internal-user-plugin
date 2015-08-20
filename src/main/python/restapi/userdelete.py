import org.codehaus.jettison.json.JSONObject
import os
from com.xebialabs.deployit.engine.api.security import User
from com.xebialabs.deployit.security import PermissionDeniedException
from org.apache.jackrabbit.api.security.user import AuthorizableExistsException 
from com.xebialabs.deployit.jcr import RuntimeRepositoryException
try:
	username = request.entity['username']
	userService.delete(username)
	print "User deleted successfully !!"
	# list user's roles and unassign
	for item in roleService.listRoles(username):
		roleService.unassign(item,username)	
except PermissionDeniedException, e:
    print e.message

