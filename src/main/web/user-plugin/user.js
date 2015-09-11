angular
		.module('usermanagement', [])
		.config(
				function($httpProvider) {

					// The following code retrieves credentials from the main XL Deploy application
					// and tells AngularJS to append them to every request.
					var flexApp = parent.document
							.getElementById("flexApplication");
					if (flexApp)
						$httpProvider.defaults.headers.common.Authorization = flexApp
								.getBasicAuth();

				})
		.controller(
				'UserController',
				function($http, $scope) {
					

					$scope.save = function() {
						var dataObj = {
							"username" : $scope.username,
							"password" : $scope.password,
							"adminFlag" : $scope.adminFlag,
							"selRoles" : $scope.selRoles
						};
						$http.post('/api/extension/user', dataObj).
							  success(function(data, status, headers, config) {
					    			$scope.stdout = data.stdout;
									$scope.response = data.entity;
									$scope.status = status									
							  }).
							  error(function(data, status, headers, config) {
							    	$scope.stdout = data.stdout;
									$scope.response = data.entity;
									$scope.status = status									
							  });							
					};
					$scope.delete = function() {
						var dataObj = {
							"username" : $scope.username
						};
						$http.post('/api/extension/userdelete', dataObj).
							  success(function(data, status, headers, config) {
					    			$scope.stdout = data.stdout;
									$scope.response = data.entity;
									$scope.status = status									
							  }).
							  error(function(data, status, headers, config) {
							    	$scope.stdout = data.stdout;
									$scope.response = data.entity;
									$scope.status = status									
							  });							
					};
					$scope.validate = function() {
						var dataObj = {
							"ldapURL" : $scope.ldapURL,
							"managerDn" : $scope.managerDn,
							"managerPassword" :$scope.managerPassword,
							"userBase" :$scope.userBase,
							"userDn" :$scope.userDn
						};
						$http.post('/api/extension/ldapvalidate', dataObj).
							  success(function(data, status, headers, config) {
					    			$scope.result = data.stdout;
									$scope.status = status
							  }).
							  error(function(data, status, headers, config) {
							    	$scope.result = data.stdout;
									$scope.status = status
							  });							
					};
					$scope.loadRoles = function() {
						$http
								.get('/deployit/security/role')
								.then(
										function(response) {
											// response.data.entity is the serialized version of what Jython script puts into
											// response.entity in the script.
											$scope.rolesList = response.data;
										});
					};
					$scope.selRoles = {}
					$scope.loadRoles();
				});
