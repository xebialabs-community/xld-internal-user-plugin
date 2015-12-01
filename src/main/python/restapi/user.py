from com.xebialabs.deployit.security import PermissionDeniedException
from com.xebialabs.deployit.jcr import RuntimeRepositoryException
from com.xebialabs.deployit.engine.api.security import User

username = request.entity['username']
password = request.entity['password']
try:
	adminFlag = request.entity['adminFlag']
except:
	adminFlag = False

newUser = User(username,adminFlag)
newUser.setPassword(password)

try:
	userService.create(username,newUser)
	print "Created new user successfully !!"
except RuntimeRepositoryException, e:
	print "User exists so modifying password and roles !!"
	userService.modifyPassword(username,newUser)

	roles = request.entity['selRoles']
	# list user's roles and unassign
	for item in roleService.listRoles(username):
		roleService.unassign(item,username)
	# add new roles
	for item in roles:
		if roles[item] == True:
			roleService.assign(item,username)

except PermissionDeniedException, e:
	print e.message
