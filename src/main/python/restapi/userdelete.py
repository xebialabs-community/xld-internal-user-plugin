from com.xebialabs.deployit.security import PermissionDeniedException
try:
	username = request.entity['username']
	userService.delete(username)
	print "User deleted successfully !!"
	# list user's roles and unassign
	for item in roleService.listRoles(username):
		roleService.unassign(item,username)	
except PermissionDeniedException, e:
	print e.message

