import org.codehaus.jettison.json.JSONObject
import os
from com.xebialabs.deployit.engine.api.security import User
#response.entity = request.entity
username = request.entity['username']
userService.delete(username)
print "User deleted successfully !!"
# list user's roles and unassign
for item in roleService.listRoles(username):
	roleService.unassign(item,username)	

